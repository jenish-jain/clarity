
import type { Metadata } from "next";
import { Radio_Canada } from "next/font/google";
import "./globals.css";

const font = Radio_Canada({ subsets: ["canadian-aboriginal"] });

export const metadata: Metadata = {
  title: "Clarity",
  description: "A simple app to give you clarity on your expenses",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={font.className}>{children}</body>
    </html>
  );
}
