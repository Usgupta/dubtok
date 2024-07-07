import React from "react";
import Image from 'next/image'
import { IBM_Plex_Mono } from "next/font/google";
import Link from 'next/link'
export default function Navbar(){
    return(
        <nav>
            <div className="bg-black h-[10vh] rounded-xm flex flex-row items-center font-default font-bold">
            <Link href="/"> <Image src="/logo-white2.png" className='pl-5' width= {2000 / 10} height={439 / 10} /></Link>
            <p className="ml-auto text-3xl pr-10">About</p>
            </div>
        </nav>
      )

}
