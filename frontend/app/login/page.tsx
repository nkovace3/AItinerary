import { MapPin } from "lucide-react";
import { SignInButton } from "@/components/sign-in-button";
import { AmbientGlow } from "@/components/ambient-glow";

export default function LogIn() {
  return (
    <div className="relative flex flex-1 items-center justify-center overflow-hidden px-4 py-12">
      <AmbientGlow />

      <div className="w-full max-w-sm rounded-3xl border border-border/60 bg-card/80 p-8 shadow-2xl backdrop-blur-xl">
        <div className="flex flex-col items-center gap-6 text-center">
          <div className="flex size-12 items-center justify-center rounded-2xl bg-primary text-primary-foreground shadow-sm">
            <MapPin className="size-6" />
          </div>

          <div className="flex flex-col gap-2">
            <h1 className="text-3xl font-bold tracking-tight text-foreground">
              Welcome to <span className="text-primary">AI</span>tinerary
            </h1>
            <p className="text-sm text-muted-foreground">
              Turn the places you already saved on Google Maps into a
              personalized, AI-planned itinerary for your city.
            </p>
          </div>

          <SignInButton className="w-full" />

          <p className="text-xs text-muted-foreground">
            We only use your saved places to plan your trips — nothing else.
          </p>
        </div>
      </div>
    </div>
  );
}
