from schemas.rss_results import RSS_Results

async def research_story(article: RSS_Results):
    
    return f"Research summary for article titled '{article.title}' from {article.source}."