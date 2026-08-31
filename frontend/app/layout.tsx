import "./globals.css"; import Link from "next/link";
export const metadata={title:"ENDLINE — Dependency Registry",description:"Consensus-backed dependency lifecycle registry"};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body><header><Link href="/" className="brand">ENDLINE</Link><nav><Link href="/">Registry</Link><Link href="/register">Register</Link><Link href="/about">About</Link></nav><span className="network">STUDIONET / 61999</span></header>{children}</body></html>}
