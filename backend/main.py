from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, HTTPException
from services.rss import get_nba_headlines
from services.pipeline import process_article_pipeline

from schemas.outputs import ArticleResponse

from database import SessionLocal
from repository import save_article, get_all_articles, get_article

app = FastAPI()

@app.get("/")
async def get_nba():
    article = await get_nba_headlines()
    story = await process_article_pipeline(article)
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