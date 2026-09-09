import { AmbientGlow } from "@/components/ambient-glow";
import { PlacePreferences } from "@/components/place-preferences";

export default function Welcome() {
  return (
    <section className="relative flex flex-1 items-center justify-center overflow-hidden px-4 py-12">
      <AmbientGlow />
      <PlacePreferences />
    </section>
  );
}
