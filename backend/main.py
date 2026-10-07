from fastapi import FastAPI
from api.routes import articles

app = FastAPI()

app.include_router(articles.router)