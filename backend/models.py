from datetime import datetime

from sqlalchemy import String, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column
from pgvector.sqlalchemy import Vector

from database import Base

class Article(Base):
    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String, unique=True)
    published_at: Mapped[datetime] = mapped_column(DateTime)
    source: Mapped[str] = mapped_column(String)
    category: Mapped[str] = mapped_column(String, nullable=False)

    headline: Mapped[str] = mapped_column(String)
    summary: Mapped[str] = mapped_column(String)
    key_points: Mapped[list[str]] = mapped_column(JSON)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    dynamics: Mapped[dict] = mapped_column(JSON, nullable=True)

    embedding: Mapped[list[float]] = mapped_column(Vector(768), nullable=True)
