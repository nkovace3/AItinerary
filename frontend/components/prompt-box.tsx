import { Textarea } from "@/components/ui/textarea"
import { SendHorizontal } from "lucide-react"
import { FieldLabel } from "@/components/ui/field"
import { auth } from "@/lib/auth";
import { headers } from "next/headers";

export async function PromptBox() {
    const session = await auth.api.getSession({
        headers: await headers(),
    });

    const name = session?.user.name;

    const hours = new Date().getHours();
    const timeOfDay = hours >= 4 && hours < 11 ? "morning" : hours >= 11 && hours < 16 ? "afternoon" : hours >= 16 || hours < 4 ? "evening" : "day";


    return (
        <section className="mx-auto grid w-full max-w-xl grid-cols-[1fr_auto] gap-x-2 gap-y-4">
            <FieldLabel htmlFor="feedback" className="col-start-1 row-start-1 w-full text-center text-3xl font-bold tracking-tight text-foreground">
                {name ? `Where would you like to explore this ${timeOfDay}, ${name}?` : `Where would you like to explore this ${timeOfDay}?`}
            </FieldLabel>
            <Textarea id="feedback" className="col-start-1 row-start-2 min-w-0 max-h-52 resize-none overflow-y-auto" />
            <SendHorizontal className="col-start-2 row-start-2 size-5 shrink-0 self-center" />
        </section>
    )
}