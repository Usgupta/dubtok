"use client";
import React, { useState } from "react";
import { Poppins } from 'next/font/google'
import DragBox from "./DragBox";
import Uploadfile from "./Uploadfile";
import FormDrop  from "./Dropdown";
import SmallButton from "./SmallButton"
import {uploadVideoFile, fetchResults} from "../utils/api"
export default function FileForm(){
    const [fileState, setFileState] = useState("inactive");
    const [videoFile, setVideoFile] = useState();
    const [dubType, setDub] = useState();
    function setFile(file){
        setFileState("active")
        setVideoFile(file)
    }
    function sendFile(){
        uploadVideoFile(videoFile, dubType);
    }
    return (
    
        <div className={` transition-all duration-300 ${(fileState == "active" ? "h-[700px] w-[900px] p-5 pt-10" : "h-[500px] w-[700px] p-10")} bg-lightgrey border-black border-2 drop-shadow-xl rounded-[18px] flex flex-col items-center justify-between`}>
            <h1 className='font-medium text-4xl w-[90%] mb-2'>Translate your Content</h1>
            <Uploadfile setFile = {setFile}/>
            <div className="w-[80%] flex flex-row items-center justify-end">
                <FormDrop setDub = {setDub}/>
                <SmallButton onClick={sendFile} text="Dub It!" className="ml-10 bg-purple hover:bg-darkpurple drop-shadow-lg"/>
            </div>
            
        </div>
    )
    }       