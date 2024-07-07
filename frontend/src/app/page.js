"use client";
import FileForm  from "./components/FileForm";
import DragBox from "./components/DragBox";
import Button from "./components/Button";
import MainDescription from "./components/MainDescription";
import Image from 'next/image'
import Head from "next/head";
export default function Home() {
  return (
    <main className="relative overflow-hidden h-[90vh] flex flex-row lg:mt:0 lg:items-center justify-center">
      <MainDescription className="mt-20 md:mt-0"/>
      <div className='w-[200px] lg:w-[304px] mt-20 md:mt-0'>
      <Image src="/Prototype.png" width= {276 * 1.1} height={448 * 1.1} alt="Prototype Image" />
      </div>

    </main>
  );
}
