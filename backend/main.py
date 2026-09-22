from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, HTTPException
from services.rss import get_latest_articles, feeds
from services.pipeline import process_article, run_ingestion

from schemas.outputs import ArticleResponse

from database import SessionLocal
from repository import save_article, get_all_articles, get_article

app = FastAPI()

@app.get("/")
async def get_nba():
    article = await get_latest_articles()
    story = await process_article(article)
    db = SessionLocal()
    try:
        saved_article = await save_article(
            db=db,
            article=article,
            story=story
        )

        return {
            "message": "Test",
            "article_id": saved_article.id,
            "category": saved_article.category,
            "research": story,
        }
    finally:
        db.close()

@app.get("/test")
async def test():
    # for feed in feeds:
    #     articles = await get_latest_articles(feed)

    #     print(f"\n{feed['category']}: {len(articles)} articles")

    #     for article in articles[:3]:
    #         print(article.title)
    #         print(article.category)
    await run_ingestion()


@app.get("/articles", response_model=list[ArticleResponse])
async def read_articles():
    db = SessionLocal()

    try:
        return await get_all_articles(db)
    finally:
        db.close()

@app.get("/articles/{article_id}", response_model=ArticleResponse)
async def read_article(article_id: int):
    db = SessionLocal()

    try:
        article =  await get_article(db, article_id)

        if article is None:
            raise HTTPException(
                status_code=404,
                detail="Article not found"
            )

        return article
    finally:
        db.close()