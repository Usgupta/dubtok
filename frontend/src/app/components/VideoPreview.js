'use client'
import { React, Suspense, useState, useEffect, useRef} from "react";
import Loading from "./Loading";

export default function VideoPreview({videoFile}){

    var [widthName, setWidth] = useState()
    var video = document.createElement('video');
    var src = videoFile;
    video.src = src
    video.onloadedmetadata = () => {
        console.log("done")
        var width = video.videoWidth;
        var height = video.videoHeight;
        setWidth((width >= height) ? "w-[90%]" : "h-[80%]")
    };
   
   
        
    return(
        <video
        className={widthName} controls>
        <source src={videoFile}/>
        </video> 
    )
    
}