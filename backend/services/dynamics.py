from services.google import execute_query, create_embedding
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

SITUATION_DESCRIPTIONS = {
    "departure": "a person or group leaves an existing group or organization",
    "arrival": "a new person or group enters an existing group or organization",
    "conflict": "two or more parties are in conflict",
    "competition": "two or more parties are competing",
    "collaboration": "two or more parties are working together",
    "acquisition": "one organization takes control of another",
    "loss": "an important person, resource, or position is lost",
    "recovery": "a person, group, or organization recovers from a setback",
    "rise": "a person, group, or organization gains status or influence",
    "decline": "a person, group, or organization loses status or influence",
    "transformation": "the structure or identity of something changes",
    "negotiation": "two or more parties are negotiating",
    "crisis": "the situation involves significant instability or threat",
    "controversy": "the situation involves significant disagreement or dispute",
    "discovery": "new information or an important finding emerges",
    "milestone": "a major achievement or significant event occurs",
    "continuity": "an existing group or structure largely remains intact",
    "transition": "a person, group, or organization moves from one state to another",
}


RELATIONSHIP_DESCRIPTIONS = {
    "individual-individual": "the situation involves a relationship between two individuals",
    "individual-group": "an individual is connected to or interacting with a group",
    "individual-organization": "an individual is connected to or interacting with an organization",
    "group-group": "two groups are connected to or interacting with each other",
    "organization-organization": "two organizations are connected to or interacting with each other",
    "leader-followers": "a leader has a relationship with a group of followers",
    "rivals": "two or more parties are rivals",
    "buyer-seller": "one party is buying from or selling to another party",
}


ACTION_DESCRIPTIONS = {
    "join": "a person or group joins another group",
    "leave": "a person or group leaves an existing group",
    "replace": "one member takes the place of another",
    "acquire": "one organization takes ownership or control of another",
    "sell": "a person or organization sells something to another party",
    "fire": "an organization removes a member",
    "hire": "an organization brings in a new member",
    "promote": "a person gains a higher position or status",
    "demote": "a person loses position or status",
    "compete": "two or more parties compete with one another",
    "negotiate": "two or more parties negotiate with one another",
    "accuse": "one party accuses another of wrongdoing",
    "invest": "a person or organization commits resources toward something",
    "withdraw": "a person or organization pulls away from something",
    "announce": "a person or organization publicly announces something",
    "restructure": "an organization changes its internal structure",
    "challenge": "one party challenges another",
    "support": "one party provides support to another",
    "retain": "existing members or elements are kept",
}


POWER_DESCRIPTIONS = {
    "power_shift": "the balance of power changes",
    "power_imbalance": "one party has substantially more power than another",
    "loss_of_control": "a party loses control over a situation or resource",
    "gain_of_control": "a party gains control over a situation or resource",
    "leverage": "one party has leverage over another",
    "dependency": "one party depends on another",
    "status_change": "the status of one or more parties changes",
    "competition": "parties are competing for power, status, or resources",
    "coalition": "multiple parties form or maintain an alliance",
}


EMOTIONAL_DESCRIPTIONS = {
    "loyalty": "the situation involves loyalty to an existing person or group",
    "betrayal": "the situation involves a perceived betrayal",
    "rivalry": "the situation involves an ongoing rivalry",
    "surprise": "the situation involves an unexpected development",
    "uncertainty": "the outcome or future is uncertain",
    "excitement": "the situation involves excitement about a development",
    "anger": "the situation involves anger",
    "disappointment": "the situation involves disappointment",
    "hope": "the situation involves optimism about the future",
    "fear": "the situation involves fear about a potential outcome",
    "celebration": "the situation involves celebration of an achievement",
    "resentment": "the situation involves lingering resentment",
    "reconciliation": "the situation involves parties repairing a relationship",
}

async def embed_dynamics(dynamics: StoryDynamics) -> list[float]:
    parts = []
    
    for situation in dynamics.situation:
        description = SITUATION_DESCRIPTIONS.get(situation)

        if description:
            parts.append(description.capitalize() + ".")

    for relationship in dynamics.relationships:
        description = RELATIONSHIP_DESCRIPTIONS.get(relationship)

        if description:
            parts.append(description.capitalize() + ".")

    for action in dynamics.actions:
        description = ACTION_DESCRIPTIONS.get(action)

        if description:
            parts.append(description.capitalize() + ".")

    for power_dynamic in dynamics.power_dynamics:
        description = POWER_DESCRIPTIONS.get(power_dynamic)

        if description:
            parts.append(description.capitalize() + ".")

    for emotional_dynamic in dynamics.emotional_dynamics:
        description = EMOTIONAL_DESCRIPTIONS.get(emotional_dynamic)

        if description:
            parts.append(description.capitalize() + ".")

    text = " ".join(parts)

    response = await create_embedding(text)

    return response.embeddings[0].values
