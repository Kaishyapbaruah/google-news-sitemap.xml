import feedparser # type: ignore
from datetime import datetime, timedelta, timezone

# Blogger RSS feeds
FEEDS = [
    {"url": "https://www.jobcareerx.com/feeds/posts/default?alt=rss", "title": "Latest Posts"},
    {"url": "https://www.jobcareerx.com/feeds/posts/default/-/New%20Update?alt=rss", "title": "New Updates"},
    {"url": "https://www.jobcareerx.com/feeds/posts/default/-/Result?alt=rss", "title": "Results"},
    {"url": "https://www.jobcareerx.com/feeds/posts/default/-/Articles?alt=rss", "title": "Articles"},
    {"url": "https://www.jobcareerx.com/feeds/posts/default/-/Trending?alt=rss", "title": "Trending Topics"}
]

now = datetime.now(timezone.utc)
news_limit = now - timedelta(days=2)  # Only last 48h for Google News

xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
xml += '        xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">\n\n'

for feed in FEEDS:
    f = feedparser.parse(feed["url"])
    for entry in f.entries:
        pub_date = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
        if pub_date > news_limit:
            xml += '  <url>\n'
            xml += f'    <loc>{entry.link}</loc>\n'
            xml += '    <news:news>\n'
            xml += '      <news:publication>\n'
            xml += '        <news:name>JobCareerX</news:name>\n'
            xml += '        <news:language>en</news:language>\n'
            xml += '      </news:publication>\n'
            xml += f'      <news:publication_date>{pub_date.isoformat()}</news:publication_date>\n'
            xml += f'      <news:title>{entry.title}</news:title>\n'
            xml += '    </news:news>\n'
            xml += '  </url>\n\n'

xml += '</urlset>'

with open("google-news-sitemap.xml", "w", encoding="utf-8") as f:
    f.write(xml)

print("✅ Google News sitemap generated successfully!")
