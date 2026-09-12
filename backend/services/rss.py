import feedparser
from schemas.rss_results import RSSResult
from dateutil import parser
from dateutil.tz import gettz

ESPN_NBA_RSS_URL = "https://www.espn.com/espn/rss/nba/news"
tzinfos = {"EST": gettz("America/New_York")}

async def get_nba_headlines() -> list[RSSResult]:
    feed = feedparser.parse(ESPN_NBA_RSS_URL)
    articles = []
    for entry in feed.entries:
        article = RSSResult(
            title=entry.title,
            url=entry.link,
            published_at=parser.parse(entry.published, tzinfos=tzinfos),
            summary=entry.summary,
            source="ESPN"
        )
        articles.append(article)
    return articles[0]