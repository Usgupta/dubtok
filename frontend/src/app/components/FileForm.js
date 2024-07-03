"use client";
import React, { useState } from "react";
import { Poppins } from 'next/font/google'
import DragBox from "./DragBox";
import Uploadfile from "./Uploadfile";
import FormDrop  from "./Dropdown";
import Button from "./Button";
export default function FileForm(){
    const [fileState, setFile] = useState("inactive");
    return (
        <div className={` transition-all duration-300 ${(fileState == "active" ? "h-[700px] w-[900px] p-5 pt-10" : "h-[500px] w-[700px] p-10")} bg-lightgrey border-black border-2 drop-shadow-xl rounded-[18px] flex flex-col items-center justify-between`}>
            <h1 className='font-medium text-4xl w-[90%] mb-2'>Translate your Content</h1>
            <Uploadfile setFile = {setFile}/>
            <div className="w-[80%] flex flex-row items-center justify-center"><FormDrop/><Button  text="Dub It!" className="ml-auto bg-purple hover:bg-darkpurple drop-shadow-lg"/></div>
            
        </div>
    )
    }       