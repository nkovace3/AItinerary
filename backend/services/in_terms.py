from services.google import execute_query
from schemas.outputs import FinalStory, StoryDynamics, InTermsResult
from models import Article

async def generate_in_terms(story: FinalStory, dynamics: StoryDynamics, target_term: str, similar_article, similar_dynamics: StoryDynamics | None) -> InTermsResult:
    prompt = f"""
                You are translating a real news story into the language of another domain.

Your task is to explain the ORIGINAL STORY "in terms of" {target_term}.

The ORIGINAL STORY is the source of truth.

The RETRIEVED TARGET-DOMAIN STORY is a real example that should help you
understand how similar underlying dynamics appear in {target_term}.

Use the retrieved story as an analogy reference, but do not copy its facts
or invent a new scenario.


                ORIGINAL STORY:
                {story.model_dump_json(indent=2)}


                ORIGINAL STORY DYNAMICS:
                {dynamics.model_dump_json(indent=2)}


                TARGET DOMAIN:
                {target_term}

                RETRIEVED TARGET-DOMAIN STORY:
                {f"""Headline: {similar_article.headline}\n
                    Summary: {similar_article.headline}\n
                    Key Points: {similar_article.key_points}\n""" 
                    if similar_article else 
                    "No example is available. Use your general knowledge of the target domain."}

                RETRIEVED TARGET-DOMAIN DYNAMICS:
                {similar_dynamics.model_dump_json(indent=2) if similar_dynamics else "NO MATCH AVAILABLE"}

                INSTRUCTIONS:

1. Identify the core event in the original story.

2. Compare its underlying dynamics with the retrieved target-domain story.

3. Explain the original event using recognizable language, roles, and social
   dynamics from {target_term}.

4. Keep the original facts intact.

5. Do not invent events, people, relationships, motivations, consequences,
   locations, or circumstances.

6. Do not create a fictional target-domain story.

7. Do not simply replace the original people with people from the retrieved
   story.

8. The retrieved story should influence the analogy, but its factual details
   must not be transferred to the original story.

9. If no retrieved story exists, use general knowledge of {target_term} to
   create the analogy.

10. Use the dynamics to identify the meaningful structural similarity, but
    do not force every dynamics label into the output.

11. Keep the result concise: approximately 2–3 sentences.

12. Make it feel natural and recognizable to someone familiar with
    {target_term}.

13. Avoid forced humor, excessive slang, memes, emojis, and speculation.

Before returning the answer, make sure you are describing the ORIGINAL STORY
through a {target_term} lens rather than inventing a new story.

The "term" field MUST be exactly "{target_term}".

Return only the structured InTermsResult.
"""
    
    response = await execute_query(prompt, InTermsResult)
    return InTermsResult.model_validate_json(response.text)