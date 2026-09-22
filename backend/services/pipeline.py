from services.researcher import research_article, synthesize_search
from services.editor import edit_story
from services.rss import get_latest_articles, feeds
from schemas.rss import RSSResult
from database import SessionLocal
from repository import save_article, article_exists

async def run_ingestion():
    db = SessionLocal()

    try:
        for feed in feeds:
            articles = await get_latest_articles(feed)

            for article in articles:
                if await article_exists(db, article.url):
                    print(f'Skipping existing article: {article.title}')
                    continue
                try:
                    story = await process_article(article)
                    await save_article(db=db, article=article, story=story)
                    print(f"Saved: {article.title}")
                except Exception as e:
                    print(f"Failed: {article.title}")
                    print(e)
    finally:
        db.close()

async def process_article(article: RSSResult):
    intermediary_research = await research_article(article)

    research_resutls = await synthesize_search(intermediary_research)

    final_story = await edit_story(research_resutls)

    return final_story