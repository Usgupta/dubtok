"use client";
import FileForm  from "./components/FileForm";
import DragBox from "./components/DragBox";
import Button from "./components/Button";
import MainDescription from "./components/MainDescription";
import { Main } from "next/document";
import Image from 'next/image'
export default function Home() {
  return (
    <main className="relative overflow-hidden h-[90vh] flex flex-row items-center justify-center">
      <MainDescription/><Image src="/prototype.png"  width= {276 * 1.5} height={448 * 1.5} />
    </main>
  );
}
  