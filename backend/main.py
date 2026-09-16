from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from services.rss import get_nba_headlines
from services.researcher import research_article
from services.editor import edit_story

app = FastAPI()

@app.get("/")
async def get_nba():
    # articles = await search_web("Brunson joins Brady, Manning, Jordan and other athletes in hosting 'Saturday Night Live'")
    article = await get_nba_headlines()
    research = await research_article(article)
    final_story = await edit_story(research)
    return {"message": "Test", "research": final_story}