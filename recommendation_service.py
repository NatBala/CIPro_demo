import json
import re
from pathlib import Path
from typing import Dict, List, Set

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

DATA_DIR = Path(__file__).parent
ADVISORS_PATH = DATA_DIR / "advisors.json"
ARTICLES_PATH = DATA_DIR / "articles.json"
FEED_STATE_PATH = DATA_DIR / "feed_state.json"

if not ADVISORS_PATH.exists():
    raise RuntimeError("Missing advisors.json")
if not ARTICLES_PATH.exists():
    raise RuntimeError("Missing articles.json")

ADVISORS: List[Dict] = json.loads(ADVISORS_PATH.read_text(encoding="utf-8"))
ARTICLES: List[Dict] = json.loads(ARTICLES_PATH.read_text(encoding="utf-8"))
ARTICLE_INDEX: Dict[str, Dict] = {article["id"]: article for article in ARTICLES}

# Build firm lookup
FIRM_TO_ADVISORS: Dict[str, Set[str]] = {}
for advisor in ADVISORS:
    firm = advisor.get("firm", "").strip().lower()
    if not firm:
        continue
    FIRM_TO_ADVISORS.setdefault(firm, set()).add(advisor["id"])

DEFAULT_FEED: List[str] = [article["id"] for article in ARTICLES[:8]]

# Ensure feed state exists
if FEED_STATE_PATH.exists():
    FEED_STATE: Dict[str, List[str]] = json.loads(FEED_STATE_PATH.read_text(encoding="utf-8"))
else:
    FEED_STATE = {advisor["id"]: DEFAULT_FEED for advisor in ADVISORS}
    FEED_STATE_PATH.write_text(json.dumps(FEED_STATE, indent=2), encoding="utf-8")


def save_feed_state() -> None:
    FEED_STATE_PATH.write_text(json.dumps(FEED_STATE, indent=2), encoding="utf-8")


TICKER_REGEX = re.compile(r"\b[A-Z]{3,5}\b")


class PromptRequest(BaseModel):
    prompt: str


class FeedResponse(BaseModel):
    advisor_id: str
    articles: List[Dict]


class PromptResponse(BaseModel):
    tickers: List[str]
    firms: List[str]
    advisors_impacted: List[Dict]
    articles_recommended: List[Dict]


def parse_prompt(prompt: str) -> Dict[str, List[str]]:
    prompt_lower = prompt.lower()
    # tickers
    tickers = {token for token in TICKER_REGEX.findall(prompt) if token.upper() in {
        tag.upper() for article in ARTICLES for tag in article.get("tags", [])
    }}
    # firms
    firms = [firm for firm in FIRM_TO_ADVISORS.keys() if firm in prompt_lower]
    return {"tickers": sorted(tickers), "firms": firms}


def select_articles(tickers: List[str], firms: List[str]) -> List[Dict]:
    if tickers:
        ticker_set = {ticker.upper() for ticker in tickers}
        matches = [article for article in ARTICLES if any(tag.upper() in ticker_set for tag in article.get("tags", []))]
    else:
        matches = []
    if not matches and firms:
        matches = [article for article in ARTICLES if any(firm in article.get("summary", "").lower() for firm in firms)]
    if not matches:
        matches = ARTICLES[:8]
    return matches[:8]


def impacted_advisors(firms: List[str]) -> List[Dict]:
    if not firms:
        return ADVISORS
    impacted_ids = set()
    for firm in firms:
        impacted_ids.update(FIRM_TO_ADVISORS.get(firm, set()))
    if not impacted_ids:
        return ADVISORS
    return [advisor for advisor in ADVISORS if advisor["id"] in impacted_ids]


app = FastAPI(title="Advisor Recommendation Service", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
    ,
    allow_headers=["*"]
)


@app.get("/api/advisors")
def get_advisors():
    return {"advisors": ADVISORS}


@app.get("/api/articles")
def get_articles():
    return {"articles": ARTICLES}


@app.get("/api/feeds/{advisor_id}")
def get_feed(advisor_id: str):
    article_ids = FEED_STATE.get(advisor_id)
    if not article_ids:
        article_ids = DEFAULT_FEED
    articles = [ARTICLE_INDEX.get(article_id) for article_id in article_ids if ARTICLE_INDEX.get(article_id)]
    return {"advisor_id": advisor_id, "articles": articles}


@app.get("/api/feeds")
def get_all_feeds():
    return {
        advisor_id: [ARTICLE_INDEX.get(article_id) for article_id in article_ids if ARTICLE_INDEX.get(article_id)]
        for advisor_id, article_ids in FEED_STATE.items()
    }


@app.post("/api/prompts", response_model=PromptResponse)
def handle_prompt(request: PromptRequest):
    prompt_text = request.prompt.strip()
    parsed = parse_prompt(prompt_text)
    advisors_list = impacted_advisors(parsed["firms"])
    articles = select_articles(parsed["tickers"], parsed["firms"])

    # Update feed state for impacted advisors
    article_ids = [article["id"] for article in articles]
    for advisor in advisors_list:
        FEED_STATE[advisor["id"]] = article_ids
    save_feed_state()

    return {
        "tickers": parsed["tickers"],
        "firms": parsed["firms"],
        "advisors_impacted": advisors_list,
        "articles_recommended": articles
    }


@app.get("/api/status")
def status():
    return {"advisors": ADVISORS, "articles": len(ARTICLES), "feeds": FEED_STATE}
