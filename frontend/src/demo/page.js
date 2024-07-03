"use client";

import { Main } from "next/document";
import Image from 'next/image'
import TranslateDescription from "@/app/components/TranslateDescription";
import Navbar from '../components/Navbar'
export default function Home() {
  return (
    <main className="bg-darkgrey h-[100vh] flex flex-row items-center justify-center">
      <Navbar/>
    </main>
  );
}
