# from dotenv import load_dotenv

# load_dotenv()

# from fastapi import FastAPI, HTTPException
# from services.rss import get_latest_articles, feeds
# from services.pipeline import process_article, run_ingestion
# from services.dynamics import extract_dynamics, dynamics_to_text
# from services.google import create_embedding
# from schemas.outputs import StoryDynamics

# from schemas.outputs import ArticleResponse, FinalStory

# from database import SessionLocal
# from repository import save_article, get_all_articles, get_article
from fastapi import FastAPI
from api.routes import articles

app = FastAPI()

app.include_router(articles.router)

# @app.get("/")
# async def get_nba():
#     article = await get_latest_articles()
#     story = await process_article(article)
#     db = SessionLocal()
#     try:
#         saved_article = await save_article(
#             db=db,
#             article=article,
#             story=story
#         )

#         return {
#             "message": "Test",
#             "article_id": saved_article.id,
#             "category": saved_article.category,
#             "research": story,
#         }
#     finally:
#         db.close()

# @app.get("/test")
# async def test():
#     dynamics = StoryDynamics(
#     situation=[
#         "milestone",
#         "continuity",
#         "departure",
#         "arrival",
#     ],
#     relationships=[
#         "organization-organization",
#     ],
#     actions=[
#         "leave",
#         "join",
#         "replace",
#         "retain",
#     ],
#     power_dynamics=[],
#     emotional_dynamics=[
#         "loyalty",
#         "celebration",
#         "hope",
#     ],
# )


#     print("Canonical text:")
#     print(await dynamics_to_text(dynamics))

#     print("\nGenerating embedding...")

#     embedding = await create_embedding(dynamics)

#     print(f"\nEmbedding dimensions: {len(embedding)}")
#     print(f"First 10 values: {embedding[:10]}")


