from pathlib import Path
path = Path(r"c:/Users/nbalasubramanian1/Desktop/experiments/test_CIPro/build_dashboard.py")
text = path.read_text(encoding="utf-8")
old = "def render_html() -> str:\r\n\r\n    articles = load_articles(CORPUS_PATH)\r\n\r\n    cards_html = render_feed_cards(articles)\r\n\r\n    return HTML.replace('<!-- FEED_CARDS -->', cards_html)\r\n"
if old not in text:
    raise SystemExit('render_html snippet not found')
text = text.replace(old, "def render_html() -> str:\r\n\r\n    return HTML\r\n")
path.write_text(text, encoding="utf-8")
