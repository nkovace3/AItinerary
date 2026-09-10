from pydantic import BaseModel
from datetime import datetime

class RSS_Results(BaseModel):
    title: str
    url: str
    published_at: datetime
    summary: str
    source: str