import asyncio

from database import SessionLocal
from services.rss import feeds, get_latest_articles
from services.pipeline import process_article
from services.dynamics import extract_dynamics, embed_dynamics
from repository import save_article, article_exists, get_article, similar_articles


async def end_to_end_with_embedding():
    db = SessionLocal()

    try:
        feed = feeds[0]

        articles = await get_latest_articles(feed)

        print(f"Found {len(articles)} RSS articles")

        for article in articles:
            print(f"Checking: {article.title}")

            if await article_exists(db, article.url):
                print("Already exists — skipping")
                continue

            print(f"Testing article: {article.title}")

            story = await process_article(article)

            print("\nFinal story:")
            print(story)

            dynamics = await extract_dynamics(story)

            print("\nDynamics:")
            print(dynamics)

            embedding = await embed_dynamics(dynamics)

            print(f"\nEmbedding dimensions: {len(embedding)}")

            saved = await save_article(
                db=db,
                article=article,
                story=story,
                dynamics=dynamics,
                embedding=embedding,
            )

            print(f"\nSaved article ID: {saved.id}")

            break

    finally:
        db.close()

async def test_similar_search():
    db = SessionLocal()

    try:
        article = await get_article(db, 5)

        if article is None:
            print("Article not found")
            return

        print(f"Query article: {article.headline}\n")

        similar = await similar_articles(
            db,
            article.embedding,
            limit=5,
        )

        for result in similar:
            print(f"{result.id}: {result.headline}")

    finally:
        db.close()



if __name__ == "__main__":
    asyncio.run(test_similar_search())

