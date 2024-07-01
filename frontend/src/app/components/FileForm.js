import React from "react";
import { Poppins } from 'next/font/google'
import DragBox from "./DragBox";

export default function FileForm(){
    return (
        <div className="h-[500px] w-[700px] bg-lightgrey border-black border-2  drop-shadow-xl rounded-[18px]">
            <h1 className='p-4 font-medium text-3xl'>Translate your Content</h1>
            <DragBox/>
        </div>
    )
}