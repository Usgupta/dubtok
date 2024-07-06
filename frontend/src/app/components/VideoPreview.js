'use client'
import { React, Suspense, useState, useEffect} from "react";
import Loading from "./Loading";

export default function VideoPreview({videoFile}){
    const [widthName, setWidth] = useState("");

    var video = document.createElement('video');
    var src = URL.createObjectURL(videoFile);
    video.src = src
    video.onloadedmetadata = () => {
        var width = video.videoWidth;
        var height = video.videoHeight;
        setWidth((width >= height) ? "w-[90%]" : "h-[80%]")
    };
   


        return(
            <video onLoad={(response) => {

                const { width, height } = response.naturalSize;
                setWidth((width >= height) ? "w-[90%]" : "w-[10%]")

                setWidth("cock")
            }}
            className={widthName} controls>
            <source src={URL.createObjectURL(videoFile)}/>
            </video>
        )

}
