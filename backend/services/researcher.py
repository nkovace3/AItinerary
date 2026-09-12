from schemas.rss_results import RSSResult
from schemas.research_results import ResearchSteps, ResearchDecision
from services.search import search_web
from services.llm import execute_query

MAX_SEARCHES = 5

async def research_article(article: RSSResult) -> ResearchSteps:
    step = ResearchSteps(
        article=article
    )

    for _ in range(MAX_SEARCHES):
        decision = await get_next_search(step)

        if decision.done:
            break

        query = decision.query.strip().lower()

        if query in (previous.strip().lower() for previous in step.searches):
            break

        results = await search_web(decision.query)

        step.searches.append(decision.query)
        step.sources.extend(results)

        print(step)

    return step

async def get_next_search(step: ResearchSteps) -> ResearchDecision:
    prompt = await build_research_prompt(step)
    response = await execute_query(prompt)
    return ResearchDecision.model_validate_json(response.text)

async def build_research_prompt(step: ResearchSteps) -> str:
    article = step.article

    previous_searches = '\n'.join(f"- {search}" for search in step.searches)
    previous_sources = '\n'.join(f"- {source.title}: {source.content}" for source in step.sources)

    return f"""
You are a research agent responsible for gathering reliable
information about a news story.

ARTICLE
Title: {article.title}
Source: {article.source}
URL: {article.url}
Summary: {article.summary}

PREVIOUS SEARCHES:
{previous_searches or "None"}

INFORMATION FOUND SO FAR:
{previous_sources or "None"}

Determine what information is still needed to understand this story.

If more research is needed, provide ONE precise web search query.

If sufficient information has been gathered, indicate that research is complete.

Do not invent information.
Do not repeat previous searches.
Prefer searches that will find primary or highly reputable sources.
    """