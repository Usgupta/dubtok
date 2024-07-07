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
    if (fileState == "inactive"){
        alert("Upload a video")
        return
    }
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

    function reset(){
        setResultState("start");
        setFileState("inactive");
    }
    if (resultState == "start"){    
        return (
    
            <div className={`mr-10 transition-all duration-300 ${(fileState == "active" ? "h-[500px] w-[250px] lg:w-[750px] p-5 pt-5 lg:pt-10" : "h-[450px] w-[400px] lg:w-[600px] p-10")} bg-lightgrey border-black border-2 drop-shadow-xl rounded-[18px] flex flex-col items-center justify-between`}>
                <h1 className='font-medium font-poppins text-lg lg:text-3xl xl:text-4xl font-bold w-[90%] mb-2'>Translate your Content</h1>
                
                <Uploadfile setFile = {setFile}/>
                <div className="w-[80%] flex flex-row items-center justify-center xl:justify-end">
                    <FormDrop setDub = {setDub}/>
                    <SmallButton onClick={sendFile} text="Submit!" className="ml-2 lg:ml-10 bg-darkpurple hover:bg-purple drop-shadow-lg"/>
                </div>
                
            </div>
        )
    }
    
    if (resultState == "end"){
        return (
            <div className={`mr-10 transition-all duration-300 ${(fileState == "active" ? "h-[400px] md:h-[550px] w-[250px] lg:w-[750px] p-5 pt-5 lg:pt-10" : "h-[450px] w-[400px] lg:w-[600px] p-10")} bg-lightgrey border-black border-2 drop-shadow-xl rounded-[18px] flex flex-col items-center justify-between`}>
        <PreviewPage videoFile={resultsURL} resetPage={reset}/>
         </div>)
    }

    }           