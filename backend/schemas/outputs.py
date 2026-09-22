from pydantic import BaseModel, ConfigDict
from schemas.search import Source
from datetime import datetime

class FinalStory(BaseModel):
    headline: str
    summary: str
    key_points: list[str]
    sources: list[Source]

class ArticleResponse(BaseModel):
    id: int
    title: str
    url: str
    published_at: datetime
    source: str
    headline: str
    summary: str
    key_points: list[str]
    created_at: datetime
    category: str

    model_config = ConfigDict(from_attributes=True)

class StoryDynamics(BaseModel):
    situation: list[str] = []
    relationships: list[str] = []
    actions: list[str] = []
    power_dynamics: list[str] = []
    emotional_dynamics: list[str] = []