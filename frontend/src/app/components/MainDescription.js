import React from "react";
import Button from "./Button";
export default function MainDescription(){
    return (
        <div className="w-[693px] h-[300px] p-[20px]  flex flex-col justify-between">
            <h1 className="font-bold text-4xl">Diversify your content</h1>
            <p className="text-xl">Dubtok empowers creators to reach a global audience by allowing their videos to be viewed in different languages</p>
        
        <div id="buttons" className="w-[400px]  flex flex-row justify-between">
        <Button color="red" text="Get Started"/> 
        <Button color="black" text="Learn More"/>
        </div>
        
        </div>
    )
}