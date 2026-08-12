import { Textarea } from "@/components/ui/textarea"
import { SendHorizontal } from "lucide-react"
import { FieldLabel } from "@/components/ui/field"

export function PromptBox() {
    return (
        <section className="mx-auto grid w-full max-w-xl grid-cols-[1fr_auto] gap-x-2 gap-y-2">
            <FieldLabel htmlFor="feedback" className="shimmer col-start-1 row-start-1 w-full text-center text-3xl">
                Where would you like to explore today?
            </FieldLabel>
            <Textarea id="feedback" className="col-start-1 row-start-2 min-w-0 max-h-52 resize-none overflow-y-auto" />
            <SendHorizontal className="col-start-2 row-start-2 size-5 shrink-0 self-center" />
        </section>
    )
}