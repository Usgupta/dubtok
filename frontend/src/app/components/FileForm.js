import React from "react";
import { Poppins } from 'next/font/google'
import DragBox from "./DragBox";
import Uploadfile from "./Uploadfile";
import FormDrop  from "./Dropdown";
import Button from "./Button";
export default function FileForm(){
    return (
        <div className="h-[500px] w-[700px] p-10 bg-lightgrey border-black border-2 drop-shadow-xl rounded-[18px] flex flex-col items-center justify-between">
            <h1 className='font-medium text-4xl w-[80%]'>Translate your Content</h1>
            <Uploadfile/>
            <div className="w-[80%] flex flex-row items-center justify-start"><FormDrop/><Button  text="Dub It!" className="ml-auto bg-purple"/></div>
            
        </div>
    )
    }   