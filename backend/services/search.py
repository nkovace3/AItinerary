from functools import lru_cache
from config import get_settings
from tavily import TavilyClient
from schemas.search_results import SearchResult

@lru_cache
def get_client() -> TavilyClient:
    return TavilyClient(api_key = get_settings().tavily_api_key)

async def search_web(query: str) -> list[SearchResult]:
    response = get_client().search(
        query=query,
        topic = 'news',
        time_range = 'week',
        max_results = 5,
        include_answer = False,
        include_raw_content = False
    )
    # print(response)
    return [
        SearchResult(
            title=result['title'],
            url=result['url'],
            content=result['content'],
            score=result['score']
        )

        for result in response['results']
    ]
