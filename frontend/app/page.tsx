import { PromptBox } from "@/components/prompt-box";
import { redirect } from "next/navigation";
import { auth } from "@/lib/auth";
import { headers } from "next/headers";
import { AmbientGlow } from "@/components/ambient-glow";

export default async function Home() {
  const session = await auth.api.getSession({
    headers: await headers(),
  });

  if (!session) {
    redirect("/login");
  }

  return (
    <section className="relative flex flex-1 items-center justify-center overflow-hidden px-4">
      <AmbientGlow />
      <PromptBox />
    </section>
  );
}
