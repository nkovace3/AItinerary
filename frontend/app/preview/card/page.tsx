import { ChevronDown } from "lucide-react";
import { OverlayNav } from "@/components/overlay-nav";
import { StoryCard } from "@/components/story-card";
import { getArticles } from "@/lib/api";

// Stand-in for the future sign-up color picker — "a color that describes you."
const PLACEHOLDER_PERSONAL_ACCENT = "oklch(0.64 0.26 322)";

// No target-category picker exists yet, so rotate through a small set of
// targets for visual variety, skipping whichever one matches the article's
// own category (the backend rejects translating a category into itself).
const TRANSLATION_TARGETS = ["Reality TV", "Finance", "Politics", "NBA", "NFL", "MLB"];

function pickTranslationTarget(category: string, index: number): string {
  for (let offset = 0; offset < TRANSLATION_TARGETS.length; offset++) {
    const candidate =
      TRANSLATION_TARGETS[(index + offset) % TRANSLATION_TARGETS.length];
    if (candidate.toLowerCase() !== category.toLowerCase()) return candidate;
  }
  return TRANSLATION_TARGETS[0];
}

export default async function CardPreview() {
  const articles = await getArticles();

  return (
    <div className="fixed inset-0 snap-y snap-mandatory overflow-y-scroll bg-background [-ms-overflow-style:none] [scrollbar-width:none] [&::-webkit-scrollbar]:hidden">
      <OverlayNav />

      {articles.map((article, i) => (
        <section
          key={article.id}
          className="relative flex h-dvh w-full snap-center snap-always items-center justify-center px-6"
        >
          <div className="w-full max-w-md">
            <StoryCard
              article={article}
              translationTarget={pickTranslationTarget(article.category, i)}
              personalAccent={PLACEHOLDER_PERSONAL_ACCENT}
            />
          </div>

          {i === 0 && (
            <div className="pointer-events-none absolute bottom-10 left-1/2 flex -translate-x-1/2 animate-bounce flex-col items-center gap-1 text-muted-foreground">
              <span className="text-xs">scroll for the next story</span>
              <ChevronDown className="size-4" />
            </div>
          )}
        </section>
      ))}
    </div>
  );
}
