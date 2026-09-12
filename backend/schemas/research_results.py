from pydantic import BaseModel
from datetime import datetime

from schemas.search_results import SearchResult
from schemas.rss_results import RSSResult

class ResearchStep(BaseModel):
    article: RSSResult
    searches: list[str] = []
    sources: list[SearchResult] = []
    facts: list[str] = []
    questions: list[str] = []

class ResearchDecision(BaseModel):
    query: str | None = None
    done: bool