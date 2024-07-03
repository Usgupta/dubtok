"use client";
import FileForm from "../components/FileForm";
import TranslateDescription from "../components/TranslateDescription";
export default function Home() {
  return (
    <main className="bg-darkgrey h-[100vh] flex flex-row items-center justify-center">
      <TranslateDescription /><FileForm/>
    </main>
  );
}
