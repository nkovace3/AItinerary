from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, HTTPException
from services.rss import get_latest_articles, feeds
from services.pipeline import process_article, run_ingestion
from services.dymanics import extract_dynamics

from schemas.outputs import ArticleResponse, FinalStory

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
    # db = SessionLocal()
    # story = await get_article(db=db, article_id=1)
    # dynamics = await extract_dynamics(story)
    # return {"result": dynamics}
    story = FinalStory(
    headline="Reality TV Star Leaves Longtime Alliance and Joins Rival Group",
    summary=(
        "After years with the same alliance, a prominent cast member "
        "leaves the group and joins a rival alliance."
    ),
    key_points=[
        "A prominent member leaves a longstanding alliance.",
        "The person joins a competing group.",
        "The move changes the balance of power between the two groups.",
    ],
    sources=[],
)


    dynamics = await extract_dynamics(story)
    print(dynamics.model_dump_json(indent=2))


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