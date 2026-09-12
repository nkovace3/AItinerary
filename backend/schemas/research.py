from pydantic import BaseModel
from datetime import datetime

from schemas.search import SearchResult
from schemas.rss import RSSResult

class ResearchPlan(BaseModel):
    questions: list[str]

class ResearchExecutionSteps(BaseModel):
    article: RSSResult
    searches: list[str] = []
    sources: list[SearchResult] = []
    # facts: list[str] = []
    questions: list[str] = []

class ResearchDecision(BaseModel):
    query: str | None = None
    done: bool

class ResearchAssessment(BaseModel):
    question: str
    answered: bool
    reasoning: str