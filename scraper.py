import feedparser

RSS_URL = "https://rsshub.app/linkedin/company/bydenergystorage"

def fetch_posts():
    feed = feedparser.parse(RSS_URL)

    data = []

    for entry in feed.entries[:5]:
        data.append({
            "title": entry.title,
            "content": entry.summary,
            "date": entry.published if hasattr(entry, "published") else ""
        })

    return data
