"use client";
import FileForm  from "./components/FileForm";
import DragBox from "./components/DragBox";
import Button from "./components/Button";
import MainDescription from "./components/MainDescription";
import { Main } from "next/document";
export default function Home() {
  return (
    <main className="bg-darkgrey h-[100vh]">
      <MainDescription/>
    </main>
  );
}
