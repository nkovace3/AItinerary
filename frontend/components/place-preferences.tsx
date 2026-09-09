"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { FieldDescription, FieldLegend, FieldSet } from "@/components/ui/field";
import { ToggleGroup, ToggleGroupItem } from "@/components/ui/toggle-group";

const PLACE_TYPES = [
  "Museums",
  "Parks & Nature",
  "Historic Sites",
  "Restaurants",
  "Cafes & Coffee",
  "Nightlife",
  "Live Music",
  "Art Galleries",
  "Local Markets",
  "Shopping",
  "Beaches",
  "Architecture",
  "Breweries & Wineries",
  "Hidden Gems",
] as const;

const MIN_SELECTIONS = 3;

export function PlacePreferences() {
  const [selected, setSelected] = useState<string[]>([]);
  const remaining = Math.max(MIN_SELECTIONS - selected.length, 0);

  return (
    <div className="flex w-full max-w-xl flex-col items-center gap-8 text-center">
      <div className="flex flex-col items-center gap-2">
        <h1 className="text-3xl font-bold tracking-tight text-foreground">
          What do you love to explore?
        </h1>
        <p className="text-sm text-muted-foreground">
          Pick at least {MIN_SELECTIONS} — we will use these to shape your
          itineraries.
        </p>
      </div>

      <FieldSet className="w-full items-center gap-4">
        <FieldLegend variant="label" className="sr-only">
          Favorite types of places
        </FieldLegend>

        <ToggleGroup
          multiple
          value={selected}
          onValueChange={setSelected}
          className="w-full flex-wrap justify-center"
        >
          {PLACE_TYPES.map((type) => (
            <ToggleGroupItem key={type} value={type} variant="outline" size="sm">
              {type}
            </ToggleGroupItem>
          ))}
        </ToggleGroup>

        <FieldDescription className="text-center text-xs">
          {remaining > 0 ? `${remaining} more to go` : "Great — you can continue"}
        </FieldDescription>
      </FieldSet>

      {/* Continue is intentionally left unwired — hook up the submit logic yourself */}
      <Button
        type="button"
        disabled={selected.length < MIN_SELECTIONS}
        className="w-full max-w-xs"
      >
        Continue
      </Button>
    </div>
  );
}
