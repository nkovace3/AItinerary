from functools import lru_cache
from config import get_settings
from google import genai
from pydantic import BaseModel
from schemas.outputs import StoryDynamics

@lru_cache
def get_client() -> genai.Client:
    return genai.Client(api_key = get_settings().google_api_key)

async def execute_query(prompt: str, schema: type[BaseModel]) -> str:
    response = get_client().models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": schema,
        },
    )

    return response

async def create_embedding(text: str) -> list[float]:
    response = get_client().models.embed_content(
        model="gemini-embedding-2",
        contents=text,
        config={
            "output_dimensionality": 768,
        },
    )

    return response