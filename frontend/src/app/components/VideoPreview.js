'use client'
import { React, Suspense, useState, useEffect, useRef} from "react";
import Loading from "./Loading";

export default function VideoPreview({videoFile, className}){

    var [widthName, setWidth] = useState()
    var video = document.createElement('video');
    var src = videoFile;
    video.src = src
    video.onloadedmetadata = () => {
        console.log("done")
        var width = video.videoWidth;
        var height = video.videoHeight;
        console.log(width)
        console.log(height)
        setWidth((width >= height) ? "w-[90%]" : "h-[70%]")
    };



    return(
        <video
        className={`${widthName} ${className}`} data-width={widthName} controls>
        <source src={videoFile}/>
        </video>
    )

}
