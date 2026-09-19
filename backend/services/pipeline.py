from services.researcher import research_article, synthesize_search
from services.editor import edit_story
from schemas.rss import RSSResult

async def process_article_pipeline(article: RSSResult):
    intermediary_research = await research_article(article)

    research_resutls = await synthesize_search(intermediary_research)

    final_story = await edit_story(research_resutls)

    return final_story