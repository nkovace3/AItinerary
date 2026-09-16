from pydantic import BaseModel
from datetime import datetime

from schemas.search import Source, SearchResult
from schemas.rss import RSSResult

class ResearchPlan(BaseModel):
    questions: list[str]

class ResearchExecutionSteps(BaseModel):
    article: RSSResult
    searches: list[str] = []
    sources: list[SearchResult] = []
    answered_questions: list[str] = []
    questions: list[str] = []

class ResearchDecision(BaseModel):
    question: str
    query: str | None = None
    done: bool

class ResearchQuestionAssessment(BaseModel):
    question: str
    answered: bool
    reasoning: str

class ResearchResult(BaseModel):
    facts: list[str] = []
    context: list[str] = []
    sources: list[Source]