from pydantic import BaseModel

class Source(BaseModel):
    title: str
    url: str

class SearchResult(BaseModel):
    source: Source
    content: str
    score: float | None = None