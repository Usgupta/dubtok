"use client";
import FileForm from "../components/FileForm";
import TranslateDescription from "../components/TranslateDescription";
import FadeIn from 'react-fade-in'
import Circle from "../components/Circle"
export default function Home() {
  return (
    
    <main className="bg-lightgrey relative overflow-hidden h-[100vh] flex flex-row items-center justify-center">
       <Circle/>
      <TranslateDescription /><FileForm/>
     
    </main>
  );
}
