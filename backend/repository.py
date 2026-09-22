from sqlalchemy.orm import Session
from sqlalchemy import select, text

from models import Article
from schemas.rss import RSSResult
from schemas.outputs import FinalStory

async def save_article(db: Session, article: RSSResult, story: FinalStory) -> Article:
    db_article = Article(
        title=article.title,
        url=article.url,
        published_at=article.published_at,
        source=article.source,
        headline=story.headline,
        summary=story.summary,
        key_points=story.key_points,
        category=article.category
    )

    db.add(db_article)
    db.commit()
    db.refresh(db_article)

    return db_article

async def get_all_articles(db: Session) -> list[Article]:
    statement = (
        select(Article)
        .from_statement(text("SELECT * FROM articles ORDER BY published_at DESC"))
    )

    return list(db.scalars(statement).all())

async def get_article(db: Session, article_id: int) -> Article | None:
    statement = (
            select(Article)
            .from_statement(text("SELECT * FROM articles WHERE id = :article_id"))
            .params(article_id=article_id)
        )
    return db.scalars(statement).first()

async def article_exists(db: Session, check_url: str) -> bool:
    statement = (
        select(Article)
        .from_statement(text("SELECT id FROM articles WHERE url = :check_url"))
        .params(check_url=check_url)
    )   
    return db.scalar(statement) is not None