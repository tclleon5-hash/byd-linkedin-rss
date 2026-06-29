from playwright.sync_api import sync_playwright
from datetime import datetime

def fetch_posts():
    url = "https://www.linkedin.com/company/bydenergystorage/posts/"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, timeout=60000)
        page.wait_for_timeout(8000)

        content = page.content()

        # 👉 如果被LinkedIn拦截
        if "sign in" in content.lower() or len(content) < 1000:
            browser.close()
            return []

        posts = page.query_selector_all("div.feed-shared-update-v2")

        data = []

        for post in posts[:5]:
            try:
                text = post.inner_text()
                data.append({
                    "title": "BYD Energy Storage Update",
                    "content": text[:300],
                    "date": datetime.utcnow().isoformat()
                })
            except:
                continue

        browser.close()
        return data
