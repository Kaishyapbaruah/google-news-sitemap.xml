# google-news-sitemap.xml
# JobCareerX Auto Google News Sitemap

This repository automatically generates a **Google News XML sitemap** from Blogger RSS feeds.

## How it works
1. `generate_sitemap.py` fetches your feeds and creates `google-news-sitemap.xml`.
2. GitHub Actions runs the workflow every 12 hours to keep the sitemap updated.
3. Submit the raw `.xml` file URL to Google Search Console.

## Sitemap URL Example
https://raw.githubusercontent.com/YOUR-USERNAME/jobcareerx-sitemap/main/google-news-sitemap.xml
