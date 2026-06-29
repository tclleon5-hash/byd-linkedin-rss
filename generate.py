import xml.etree.ElementTree as ET
from scraper import fetch_posts
from datetime import datetime

def build_rss(items):
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = "BYD Energy Storage LinkedIn"
    ET.SubElement(channel, "link").text = "https://www.linkedin.com/company/bydenergystorage/"
    ET.SubElement(channel, "description").text = "Auto generated RSS feed"

    if not items:
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = "No data (scraping failed)"
        ET.SubElement(item, "description").text = "LinkedIn returned empty content"
        ET.SubElement(item, "pubDate").text = datetime.utcnow().isoformat()
    else:
        for i in items:
            item = ET.SubElement(channel, "item")
            ET.SubElement(item, "title").text = i["title"]
            ET.SubElement(item, "description").text = i["content"]
            ET.SubElement(item, "pubDate").text = i["date"]

    tree = ET.ElementTree(rss)
    tree.write("feed.xml", encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    posts = fetch_posts()
    build_rss(posts)
