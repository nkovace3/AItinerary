from schemas.rss import RSSResult
from schemas.research import ResearchExecutionSteps, ResearchDecision, ResearchPlan
from services.search import search_web
from services.llm import execute_query

MAX_SEARCHES = 5

async def create_research_plan(article: RSSResult) -> ResearchPlan:
    prompt = f"""
You are planning research for a news story.

Your goal is to identify the key factual questions that must
be answered before an editor can accurately explain this story.

ARTICLE:
Title: {article.title}
Source: {article.source}
Summary: {article.summary}

Generate 3-6 specific research questions.

Focus on:
- what happened
- important factual details
- relevant context
- what happens next
- information necessary for a reader to understand why the story matters

Do not write the story.
Do not answer the questions.
Only identify the questions that need to be researched.
"""
    response = await execute_query(prompt, ResearchPlan)
    return ResearchPlan.model_validate_json(response.text)

async def research_article(article: RSSResult) -> ResearchExecutionSteps:
    plan = await create_research_plan(article)
    step = ResearchExecutionSteps(
        article=article,
        questions = plan.questions
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

async def get_next_search(step: ResearchExecutionSteps) -> ResearchDecision:
    prompt = await build_research_prompt(step)
    response = await execute_query(prompt, ResearchDecision)
    return ResearchDecision.model_validate_json(response.text)

async def build_research_prompt(step: ResearchExecutionSteps) -> str:
    questions = '\n'.join(f"- {question}" for question in step.questions)
    previous_searches = '\n'.join(f"- {search}" for search in step.searches)
    previous_sources = '\n'.join(f"- {source.title}: {source.content}" for source in step.sources)

    return f"""
You are a news research agent.

Your job is to gather reliable evidence needed to answer
the research questions for a news story.

ARTICLE:
Title: {step.article.title}
Source: {step.article.source}

RESEARCH QUESTIONS:
{questions}

PREVIOUS SEARCHES:
{previous_searches or "None"}

EVIDENCE FOUND:
{previous_sources or "None"}

Choose the single most important unanswered research question.

Then generate ONE precise search query designed to find
reliable information that helps answer that question.

If all important questions have sufficient evidence,
mark the research as complete.

Do not repeat previous searches.
Do not invent information.
Prefer primary and reputable sources.
"""