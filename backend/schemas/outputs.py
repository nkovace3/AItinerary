from pydantic import BaseModel
from schemas.search import Source

class FinalStory(BaseModel):
    headline: str
    summary: str
    key_points: list[str]
    sources: list[Source]