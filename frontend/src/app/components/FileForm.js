"use client";
import React, { useState } from "react";
import { Poppins } from 'next/font/google'
import DragBox from "./DragBox";
import Uploadfile from "./Uploadfile";
import FormDrop  from "./Dropdown";
import SmallButton from "./SmallButton"
import {uploadVideoFile, fetchResults, getURL} from "../utils/api"
import PreviewPage from "./Preview";
export default function FileForm(){
    const [resultState, setResultState] = useState("start")
    const [fileState, setFileState] = useState("inactive");
    const [videoFile, setVideoFile] = useState();
    const [dubType, setDub] = useState();
    const [resultsURL, setResultsURL] = useState()
    function setFile(file){
        setFileState("active")
        setVideoFile(file)
    }
    async function sendFile(){
    if (dubType != undefined){
       const uploaded = await uploadVideoFile(videoFile, dubType);
       const videoId = uploaded["video_id"];
       const dubbedVideo = await fetchResults(videoId);
       const fileName = dubbedVideo["filename"]
       const dubbedURL = getURL(videoId, dubType, fileName)
       setResultsURL(dubbedURL) ;
       setResultState("end");
    }
    else{
        alert("Select Translation Language")
    }
    }
    if (resultState == "start"){    
        return (
    
            <div className={`mr-10 transition-all duration-300 ${(fileState == "active" ? "h-[500px] w-[750px] p-5 pt-10" : "h-[450px] w-[600px] p-10")} bg-lightgrey border-black border-2 drop-shadow-xl rounded-[18px] flex flex-col items-center justify-between`}>
                <h1 className='font-medium text-4xl w-[90%] mb-2'>Translate your Content</h1>
                <Uploadfile setFile = {setFile}/>
                <div className="w-[80%] flex flex-row items-center justify-end">
                    <FormDrop setDub = {setDub}/>
                    <SmallButton onClick={sendFile} text="Dub It!" className="ml-10 bg-darkpurple hover:bg-purple drop-shadow-lg"/>
                </div>
                
            </div>
        )
    }
    
    if (resultState == "end"){
        return (<PreviewPage videoFile={resultsURL}/>)
    }

    }       