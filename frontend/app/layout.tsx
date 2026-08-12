import type { Metadata } from "next";
import { IBM_Plex_Sans } from "next/font/google";
import "./globals.css";
import { cn } from "@/lib/utils";
import { SiteNav } from "@/components/site-nav";

const ibmPlexSans = IBM_Plex_Sans({ subsets: ["latin"], variable: "--font-sans" });

export const metadata: Metadata = {
  title: "AItinerary",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html
      lang="en"
      className={cn("h-full", "antialiased", "font-sans", ibmPlexSans.variable)}
    >
      <body className="min-h-full flex flex-col">
        <header>
          <SiteNav />
        </header>
        <main className="flex-1">{children}</main>
      </body>
    </html>
  );
}
