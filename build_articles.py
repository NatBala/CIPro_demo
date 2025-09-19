import json
import re
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).parent
CORPUS_PATH = ROOT / "corpus.txt"
OUTPUT_PATH = ROOT / "articles.json"

ARTICLE_REGEX = re.compile(
    r"## ARTICLE \d+\s+"
    r"Title:\s*(?P<title>.+?)\s+"
    r"Published Date:\s*(?P<published>.+?)\s+"
    r"(?:Key URL|Link):\s*(?P<url>.+?)\s+"
    r"Content:\s*(?P<content>.+?)(?=\n\\=+|\Z)",
    re.DOTALL,
)

MD_LINK_REGEX = re.compile(r"\[(?P<label>[^\]]+)\]\((?P<url>[^\)]+)\)")
URL_REGEX = re.compile(r"https?://[^\s<>'\"]+")
WORD_REGEX = re.compile(r"[A-Za-z0-9]{3,}")
TICKER_REGEX = re.compile(r"\b[A-Z]{3,5}\b")


def clean_markdown_link(raw: str) -> str:
    match = MD_LINK_REGEX.search(raw)
    if match:
        return match.group("url").strip()
    bracket_match = re.search(r"<(https?://[^>]+)>", raw)
    if bracket_match:
        return bracket_match.group(1).strip()
    url_match = URL_REGEX.search(raw)
    return url_match.group(0).strip() if url_match else raw.strip()


def derive_tags(title: str, content: str) -> List[str]:
    tags = set()
    for ticker in TICKER_REGEX.findall(f"{title} {content}"):
        tags.add(ticker)
    for word in WORD_REGEX.findall(title):
        word_lower = word.lower()
        if len(word_lower) > 3:
            tags.add(word_lower)
    return sorted(tags)


def extract_articles(text: str) -> List[Dict[str, str]]:
    articles: List[Dict[str, str]] = []
    for match in ARTICLE_REGEX.finditer(text):
        title = match.group("title").strip()
        published = match.group("published").strip()
        raw_url = match.group("url").strip()
        content = match.group("content").strip()
        url = clean_markdown_link(raw_url)
        summary_line = ""
        for line in content.splitlines():
            clean_line = line.strip()
            if clean_line:
                summary_line = clean_line
                break
        article = {
            "id": re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-"),
            "title": title,
            "published_date": published,
            "url": url,
            "summary": summary_line,
            "tags": derive_tags(title, content),
        }
        articles.append(article)
    return articles


def main() -> None:
    if not CORPUS_PATH.exists():
        raise SystemExit(f"Corpus not found: {CORPUS_PATH}")
    corpus_text = CORPUS_PATH.read_text(encoding="utf-8")
    articles = extract_articles(corpus_text)
    OUTPUT_PATH.write_text(json.dumps(articles, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Generated {len(articles)} articles -> {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
