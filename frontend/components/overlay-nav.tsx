import { CircleUserRound } from "lucide-react";

/**
 * Minimal floating nav for full-bleed, immersive pages (the feed).
 * Deliberately not the site's main SiteNav — this floats over content
 * instead of occupying layout space, and stays neutral (no gold/personal
 * accent) so it never competes with the content underneath it.
 *
 * The profile icon is a placeholder — not wired to real auth/menu yet.
 */
export function OverlayNav() {
  return (
    <header className="pointer-events-none fixed inset-x-0 top-0 z-30 flex items-center justify-between bg-gradient-to-b from-background/80 to-transparent px-6 py-4 backdrop-blur-md">
      <span className="text-sm font-bold tracking-tight text-foreground">
        In Terms
      </span>

      <button
        type="button"
        className="pointer-events-auto flex size-8 cursor-pointer items-center justify-center rounded-full text-foreground/80 transition-colors hover:text-foreground"
      >
        <CircleUserRound className="size-6" />
      </button>
    </header>
  );
}
