"use client";
import FileForm  from "./components/FileForm";
import DragBox from "./components/DragBox";
import Button from "./components/Button";
import MainDescription from "./components/MainDescription";
import { Main } from "next/document";
import Image from 'next/image'
export default function Home() {
  return (
    <main className="bg-darkgrey h-[100vh] flex flex-row items-center justify-center">
      <MainDescription/><Image src="/prototype.png"  width= {276 * 2.7} height={448 * 2.7} />
    </main>
  );
}
