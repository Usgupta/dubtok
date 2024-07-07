"use client";
import FileForm from "../components/FileForm";
import TranslateDescription from "../components/TranslateDescription";
import Circle from "../components/Circle"
import ParticleBackground from "../components/ParticlesBackground";
export default function Home() {
  return (
    
    <main className="relative overflow-hidden h-[90vh] flex flex-row items-center justify-center">

     <Circle/>
     <TranslateDescription /><FileForm/>
    </main>
  );
}
