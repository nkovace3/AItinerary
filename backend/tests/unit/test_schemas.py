"""
Pure schema/model tests — no database, no network, no API keys required.
"""

from datetime import datetime

import pytest
from pydantic import ValidationError

from models import Article
from schemas.outputs import ArticleResponse
from schemas.rss import RSSResult


def test_rss_result_accepts_valid_data():
    article = RSSResult(
        title="Example headline",
        url="https://example.com/story",
        published_at=datetime(2026, 1, 1),
        summary="A short summary.",
        source="ESPN",
        category="NBA",
    )

    assert article.title == "Example headline"
    assert article.category == "NBA"


def test_rss_result_rejects_missing_required_field():
    with pytest.raises(ValidationError):
        # missing `url`, `published_at`, etc.
        RSSResult(title="Example headline", summary="...", source="ESPN", category="NBA")


def test_article_response_maps_from_orm_object():
    """
    ArticleResponse uses `model_config = ConfigDict(from_attributes=True)`
    specifically so it can be built directly from an `Article` ORM instance
    (as FastAPI's `response_model` does on every /articles request). This
    test exercises that mapping directly, without needing a database —
    `Article(...)` just builds a plain Python object until it's added to a
    session.
    """
    article = Article(
        id=1,
        title="Example headline",
        url="https://example.com/story",
        published_at=datetime(2026, 1, 1),
        source="ESPN",
        category="NBA",
        headline="A clearer headline",
        summary="A short summary.",
        key_points=["Point one", "Point two"],
        created_at=datetime(2026, 1, 1, 12, 0, 0),
    )

    response = ArticleResponse.model_validate(article)

    assert response.id == 1
    assert response.headline == "A clearer headline"
    assert response.key_points == ["Point one", "Point two"]
