from pydantic import BaseModel
from datetime import datetime

class RSSResult(BaseModel):
    title: str
    url: str
    published_at: datetime
    summary: str
    source: str
    category: str