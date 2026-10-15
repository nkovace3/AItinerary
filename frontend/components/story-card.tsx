"use client";

import { useState } from "react";
import { ArrowLeftRight, Sparkles } from "lucide-react";
import { cn } from "@/lib/utils";

export interface StoryCardProps {
  category: string;
  source: string;
  headline: string;
  dek: string;
  keyPoints: string[];
  translatedTarget: string;
  translatedHeadline: string;
  translatedDek: string;
  translatedKeyPoints: string[];
  /**
   * Placeholder for the user's chosen "personal color" (from the future
   * sign-up color picker). Passed as a raw OKLCH string so it can be
   * dropped straight into an inline CSS variable.
   */
  personalAccent: string;
}

export function StoryCard({
  category,
  source,
  headline,
  dek,
  keyPoints,
  translatedTarget,
  translatedHeadline,
  translatedDek,
  translatedKeyPoints,
  personalAccent,
}: StoryCardProps) {
  const [flipped, setFlipped] = useState(false);

  return (
    <div
      className="group [perspective:1800px]"
      style={{ "--personal-accent": personalAccent } as React.CSSProperties}
    >
      <div
        className={cn(
          "relative h-[460px] w-full transition-transform duration-700 ease-[cubic-bezier(0.22,1,0.36,1)] [transform-style:preserve-3d]",
          flipped && "[transform:rotateY(180deg)]"
        )}
      >
        {/* Front — neutral, original short-form story */}
        <div className="absolute inset-0 flex h-full flex-col gap-4 rounded-3xl border border-border bg-card p-6 [backface-visibility:hidden]">
          <div className="flex items-center justify-between">
            <span className="rounded-full bg-secondary px-3 py-1 text-xs font-medium text-secondary-foreground">
              {category}
            </span>
            <span className="text-xs text-muted-foreground">{source}</span>
          </div>

          <div className="flex flex-col gap-2">
            <h3 className="text-xl font-bold tracking-tight text-foreground">
              {headline}
            </h3>
            <p className="text-sm text-muted-foreground">{dek}</p>
          </div>

          <ul className="flex flex-1 flex-col gap-1.5 overflow-y-auto">
            {keyPoints.map((point) => (
              <li
                key={point}
                className="flex items-start gap-2 text-sm text-foreground"
              >
                <span className="mt-1.5 size-1 shrink-0 rounded-full bg-muted-foreground" />
                {point}
              </li>
            ))}
          </ul>

          <button
            type="button"
            onClick={() => setFlipped(true)}
            className="relative flex cursor-pointer items-center justify-center gap-2 overflow-hidden rounded-xl border border-border bg-background py-2.5 text-sm font-medium text-foreground transition-colors hover:bg-muted"
          >
            <span className="pointer-events-none absolute inset-0 -translate-x-full bg-gradient-to-r from-transparent via-white/40 to-transparent transition-transform duration-1000 ease-out group-hover:translate-x-full dark:via-white/10" />
            <Sparkles className="size-4" />
            Translate to {translatedTarget}
          </button>
        </div>

        {/* Back — translated, rendered in the reader's personal color */}
        <div
          className="absolute inset-0 flex h-full flex-col gap-4 rounded-3xl border p-6 [backface-visibility:hidden] [transform:rotateY(180deg)]"
          style={{
            borderColor: "var(--personal-accent)",
            backgroundColor: "color-mix(in oklch, var(--personal-accent) 6%, var(--card))",
          }}
        >
          <div className="flex items-center justify-between">
            <span
              className="rounded-full px-3 py-1 text-xs font-medium text-white"
              style={{ backgroundColor: "var(--personal-accent)" }}
            >
              In terms of {translatedTarget}
            </span>
            <span className="text-xs text-muted-foreground">{source}</span>
          </div>

          <div className="flex flex-col gap-2">
            <h3 className="text-xl font-bold tracking-tight text-foreground">
              {translatedHeadline}
            </h3>
            <p className="text-sm text-muted-foreground">{translatedDek}</p>
          </div>

          <ul className="flex flex-1 flex-col gap-1.5 overflow-y-auto">
            {translatedKeyPoints.map((point) => (
              <li
                key={point}
                className="flex items-start gap-2 text-sm text-foreground"
              >
                <span
                  className="mt-1.5 size-1 shrink-0 rounded-full"
                  style={{ backgroundColor: "var(--personal-accent)" }}
                />
                {point}
              </li>
            ))}
          </ul>

          <button
            type="button"
            onClick={() => setFlipped(false)}
            className="flex cursor-pointer items-center justify-center gap-2 rounded-xl border border-border bg-background py-2.5 text-sm font-medium text-foreground transition-colors hover:bg-muted"
          >
            <ArrowLeftRight className="size-4" />
            Back to original
          </button>
        </div>
      </div>
    </div>
  );
}
