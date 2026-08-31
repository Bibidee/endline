import "./globals.css";
import "./status.css";
import {Navbar} from "../components/layout/Navbar";
import {Footer} from "../components/layout/Footer";

export const metadata={title:"ENDLINE — Dependency Registry",description:"Consensus-backed dependency lifecycle registry on GenLayer Studionet"};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body><Navbar/><main className="page-shell">{children}</main><Footer/></body></html>}
