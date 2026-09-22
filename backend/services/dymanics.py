from services.llm import execute_query

from sqlalchemy.orm import Session

from models import Article
from sqlalchemy import select, text

from schemas.outputs import FinalStory, StoryDynamics

situations = [
    "departure",
    "arrival",
    "conflict",
    "competition",
    "collaboration",
    "acquisition",
    "loss",
    "recovery",
    "rise",
    "decline",
    "transformation",
    "negotiation",
    "crisis",
    "controversy",
    "discovery",
    "milestone",
    "continuity",
    "transition"
]

relationships = [
    "individual-individual",
    "individual-group",
    "individual-organization",
    "group-group",
    "organization-organization",
    "leader-followers",
    "rivals",
    "buyer-seller",
    # "employer-employee",
]

actions = [
    "join",
    "leave",
    "replace",
    "acquire",
    "sell",
    "fire",
    "hire",
    "promote",
    "demote",
    "compete",
    "negotiate",
    "accuse",
    "retain",
    "invest",
    "withdraw",
    "announce",
    "restructure",
    "challenge",
    "support",
]

power_dynamics = [
    "power_shift",
    "power_imbalance",
    "loss_of_control",
    "gain_of_control",
    "leverage",
    "dependency",
    "status_change",
    "competition",
    "coalition",
]

emotional_dynamics = [
    "loyalty",
    "betrayal",
    "rivalry",
    "surprise",
    "uncertainty",
    "excitement",
    "anger",
    "disappointment",
    "hope",
    "fear",
    "celebration",
    "resentment",
    "reconciliation",
]

async def extract_dynamics(story: FinalStory) -> StoryDynamics:
    prompt = f"""
                You are the structural analysis agent for a news platform called "In Terms".

                Your job is to identify the underlying structure of a news story.

                We are NOT interested in the specific topic, names, teams, companies,
                leagues, or other surface-level details.

                Instead, identify the underlying situations and dynamics that could exist
                in completely different domains.

                For example:

                An NBA team wins a championship, loses one important player, replaces that
                player, and brings back almost the entire championship roster.

                The underlying structure could include:
                - a major milestone
                - continuity after success
                - a transition caused by a departure
                - replacement of a departing member
                - loyalty among the remaining members

                These structural characteristics could also describe stories in
                Reality TV, Politics, Finance, NFL, or other domains.

                Your output will later be used to find structurally similar stories
                across completely different domains.

                ---

                STORY

                Headline:
                {story.headline}

                Summary:
                {story.summary}

                Key points:
                {chr(10).join(f"- {point}" for point in story.key_points)}

                ---

                CONTROLLED VOCABULARY

                You MUST select values only from the following lists.

                SITUATIONS:
                {", ".join(situations)}

                RELATIONSHIPS:
                {", ".join(relationships)}

                ACTIONS:
                {", ".join(actions)}

                POWER DYNAMICS:
                {", ".join(power_dynamics)}

                EMOTIONAL DYNAMICS:
                {", ".join(emotional_dynamics)}

                ---

                CLASSIFICATION INSTRUCTIONS

                1. SITUATIONS

                Select 1-3 situations from the SITUATIONS list.

                A story may contain multiple meaningful situations at the same time.

                Select situations that capture distinct structural aspects of the story.

                Do not select multiple labels that merely describe the same thing.

                For example, if a story involves a major achievement followed by the
                departure of one member, both "milestone" and "departure" may be relevant.

                2. RELATIONSHIPS

                Select every relationship from the RELATIONSHIPS list that is meaningfully
                present in the story.

                Multiple relationships may apply.

                Consider relationships between people, groups, and organizations.

                Do not select relationships merely because they are technically possible.

                3. ACTIONS

                Select every action from the ACTIONS list that is directly supported
                by the story.

                Multiple actions may apply.

                Do not infer actions that are not stated or reasonably implied.

                4. POWER DYNAMICS

                Select every meaningful power dynamic from the POWER DYNAMICS list.

                Multiple values may apply.

                If there is no meaningful power dynamic, return an empty list.

                5. EMOTIONAL DYNAMICS

                Select every meaningful emotional or social dynamic from the
                EMOTIONAL DYNAMICS list.

                Multiple values may apply.

                If there is no meaningful emotional dynamic, return an empty list.

                ---

                IMPORTANT RULES

                - You MUST use the controlled vocabulary provided above.
                - Do not invent new labels.
                - Do not modify the labels.
                - Do not create synonyms for the labels.
                - Focus on underlying structure rather than subject matter.
                - Do not mention specific people, teams, companies, leagues, or other
                domain-specific entities in the classifications.
                - Do not invent facts.
                - Only select dynamics reasonably supported by the story.
                - Do not select a value simply because it is available.
                - Empty lists are allowed for all list fields except SITUATIONS.
                - Keep the classification concise.
                - The goal is to produce a structural fingerprint that can be compared
                with stories from completely different domains.

                Return only the structured output.
                """

    response = await execute_query(prompt, StoryDynamics)
    return StoryDynamics.model_validate_json(response.text)