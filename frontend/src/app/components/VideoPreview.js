'use client'
import { React, Suspense, useState, useEffect} from "react";
import Loading from "./Loading";

export default function VideoPreview({videoFile}){
    const [widthName, setWidth] = useState("");

    var video = document.createElement('video');
    var src = URL.createObjectURL(videoFile);
    
   
   
        
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