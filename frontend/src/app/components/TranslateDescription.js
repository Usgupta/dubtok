import React from "react";
import Button from "./Button";


export default function TranslateDescription(){
    return (
        <div className=" w-[250px] ml-2 lg:mr-10 lg:ml-10 lg:w-[400px] xl:w-[900px] h-[150px] p-[20px] p  flex flex-col justify-between">
            <h1 className="font-bold mb-2 font-inter text-xl md:text-2xl lg:text-4xl">Translate your Video</h1>
            <p className="text-sm md:text-md lg:text-2xl">DubTok seamlessly translates your videos and dubs them with translated audio that matches your own voice. To get started, upload your video and select your target language.</p>
        </div>
    )
}