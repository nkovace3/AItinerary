import { StoryCard } from "@/components/story-card";

// Stand-in for the future sign-up color picker — "a color that describes you."
const PLACEHOLDER_PERSONAL_ACCENT = "oklch(0.64 0.26 322)";

export default function CardPreview() {
  return (
    <div className="min-h-dvh bg-background px-6 py-16">
      <div className="mx-auto mb-12 flex max-w-5xl flex-col gap-2 text-center">
        <h1 className="text-3xl font-bold tracking-tight text-foreground">
          In Terms — card prototype
        </h1>
        <p className="text-sm text-muted-foreground">
          Neutral by default. Click &quot;Translate&quot; to see it rendered in a
          placeholder personal color.
        </p>
      </div>

      <div className="mx-auto grid max-w-5xl grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {Array.from({ length: 3 }).map((_, i) => (
          <StoryCard
            key={i}
            personalAccent={PLACEHOLDER_PERSONAL_ACCENT}
            category="NBA"
            source="ESPN"
            headline="Mavericks Blindside League, Trade All-Star Guard Hours Before Deadline"
            dek="Dallas stuns the NBA by trading its franchise point guard in a deal nobody saw coming."
            keyPoints={[
              "Guard traded to a Western Conference rival in a 3-team deal",
              'Front office cited "long-term direction," fueling backlash from fans',
              "Rival team instantly becomes a title contender",
            ]}
            translatedTarget="Reality TV"
            translatedHeadline="The Fan-Favorite Just Got Blindsided — And Everyone's Taking Sides"
            translatedDek="The fan favorite just got traded off his own show — and his rival's cast just got a lot more dangerous."
            translatedKeyPoints={[
              'The star got "voted off" his own team in a surprise 3-way trade',
              'Management says it\'s "strategy" — fans are calling it a betrayal',
              "The rival alliance he got traded to just became the one to beat",
            ]}
          />
        ))}
      </div>
    </div>
  );
}
