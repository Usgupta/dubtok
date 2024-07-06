
import "./globals.css";
import Navbar from './components/Navbar'
import ParticleBackground from "./components/ParticlesBackground";
import { Poppins, Inter } from "next/font/google";

const poppins = Poppins({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-poppins',
  weight: ['100', '200', '300', '400', '500', '600', '700', '800', '900']
});

const inter =  Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
  weight: ['100', '200', '300', '400', '500', '600', '700', '800', '900']
});

export const metadata = {
  title: 'Page Title',
  description: 'Page Description',
}


export default function RootLayout({ children }) {
  return (
    <html lang="en" className={`${poppins.variable} ${inter.variable}`}>
      <body  >
        <Navbar/>
        <ParticleBackground className="overflow-hidden"/>
        {children}</body>
    </html>
  );
}
