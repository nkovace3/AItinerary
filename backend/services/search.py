import os
from tavily import TavilyClient
from schemas.search_results import SearchResult

client = TavilyClient(
    api_key=os.environ.get("TAVILY_API_KEY")
)

async def search_web(query: str) -> list[SearchResult]:
    response = client.search(
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
