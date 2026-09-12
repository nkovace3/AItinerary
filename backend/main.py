from fastapi import FastAPI
from services.rss import *
from services.search import *

app = FastAPI()

@app.get("/")
async def get_nba():
    articles = await search_web("Brunson joins Brady, Manning, Jordan and other athletes in hosting 'Saturday Night Live'")
    return {"message": "Default", "articles": articles}