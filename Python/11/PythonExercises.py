import feedparser
from datetime import datetime

# RSS Feed URL
RSS_FEED = "http://feeds.reuters.com/Reuters/worldNews"

def fetch_top_news_rss():
    feed = feedparser.parse(RSS_FEED)
    return feed.entries[:5]

def log_to_readme(articles):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("README.md", "a", encoding="utf-8") as readme:
        readme.write(f"\n## 🗓️ {now} - Top 5 World News from Reuters\n\n")
        for i, entry in enumerate(articles, 1):
            readme.write(f"{i}. [{entry.title}]({entry.link})\n")
        readme.write("\n---\n")

if __name__ == "__main__":
    print("Fetching top 5 world news from Reuters...")
    try:
        news_articles = fetch_top_news_rss()
        log_to_readme(news_articles)
        print("✅ News fetched and logged to README.md")
    except Exception as e:
        print("❌ Error:", e)
