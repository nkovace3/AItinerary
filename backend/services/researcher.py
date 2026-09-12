from schemas.rss_results import RSSResult
from schemas.research_results import ResearchStep, ResearchDecision
from search import search_web

MAX_SEARCHES = 5

def research_article(article: RSSResult) -> ResearchStep:
    step = ResearchStep(
        article=article
    )

    for _ in range(MAX_SEARCHES):
        decision = get_next_search(step)

        if decision.done:
            break

        results = search_web(decision.query)

        step.searches.append(decision.query)
        step.sources.extend(results)

    return step

def get_next_search(step: ResearchStep) -> ResearchDecision:
    return