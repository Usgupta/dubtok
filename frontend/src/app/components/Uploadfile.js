'use client'

import Dropzone, { Accept } from "react-dropzone";
import { Suspense, useState } from "react";
import Loading from "./Loading"
import VideoPreview from "./VideoPreview"
export default function Uploadfile({ setFile, filetype }) {

    const handleFileChange = (acceptedFiles) => {
        setVideoFile(acceptedFiles[0])
        setVideoState("active")
        setFile("active")
        console.log("active")
    }
    const [videoFile, setVideoFile] = useState();
    const [videoState, setVideoState] = useState("start");

    if (videoState == "active"){
        return(
            <Suspense fallback = {<Loading/>}>
            <VideoPreview videoFile={videoFile}/>
            </Suspense>
            
        )
    }
    return (
        <Dropzone onDropAccepted={handleFileChange} accept={filetype}>
            {({ getRootProps, getInputProps }) => (
                <div className="flex w-[90%] h-[50%]  bg-white border-2 border-gray-300 border-dashed rounded-md appearance-none cursor-pointer hover:border-gray-400 dark:hover:border-coldHeights-300 focus:outline-none transition-colors duration-300">
                    <div data-cy="dropzone" className="flex justify-center items-center space-x-2 w-full h-full px-3" {...getRootProps()}>
                        <input {...getInputProps()} />
                        <svg xmlns="http://www.w3.org/2000/svg" className="w-6 h-6 text-gray-600 dark:text-white" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor" strokeWidth="2">
                            <path strokeLinecap="round" strokeLinejoin="round"
                                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                        </svg>
                        <span className="font-medium text-gray-600 dark:text-white">Click to upload or drag and drop</span>
                    </div>
                </div>
            )}
        </Dropzone>
    )
}


