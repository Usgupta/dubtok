import React from "react";
import Image from 'next/image'
import { IBM_Plex_Mono } from "next/font/google";

export default function Navbar(){
    return(
        <nav>
            <div className="bg-black h-[90px] rounded-xm flex flex-row items-center font-default font-bold">
            <Image src="/logo-white.png" className='pl-5' width= {187} height={60} />
            <p className="ml-auto text-3xl pr-10">About</p>
            </div>
        </nav>
      ) 
      
}       