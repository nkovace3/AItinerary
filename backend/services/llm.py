from functools import lru_cache
from config import get_settings
from google import genai
# from schemas.research_results import ResearchDecision
from pydantic import BaseModel

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