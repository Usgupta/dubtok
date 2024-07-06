"use client";
import FileForm  from "./components/FileForm";
import DragBox from "./components/DragBox";
import Button from "./components/Button";
import MainDescription from "./components/MainDescription";
import { Main } from "next/document";
import Image from 'next/image'
export default function Home() {
  return (
    <main className="relative overflow-hidden h-[90vh] flex flex-row lg:items-center justify-center">
      <MainDescription className="mt-20 md:mt-0"/>
      <div className='w-[200px] lg:w-[276px] mt-20 md:mt-0'>
      <Image  src="/prototype.png" width= {276} height={448} />
      </div>
      
    </main>
  );
}
