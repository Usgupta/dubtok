import React from "react";
import Button from "./Button";
import Link from 'next/link'
export default function MainDescription({className}){
    return (
        <div id="mainDescription" className={`w-[200px] md:w-[600px] lg:w-[705px] h-[380px] p-[20px]  flex flex-col justify-between mr-6 ${className}`}>
            <h1 className="font-bold leading-relaxed font-inter text-xl md: text-4xl lg:text-6xl">Amplify your presence globally with Dubtok</h1>
            <p className=" font-inter my-3 text-sm md:text-xl lg:text-2xl">Dubtok automatically translates and dubs your video into multiple languages, making it easier for viewers worldwide to enjoy your content.</p>
        
        <div id="buttons" className="w-[200px] md:w-[400px] flex flex-col md:flex-row justify-between">
            <Link href="/demo"><Button className="bg-red hover:bg-darkred my-2  md:mr-2 md:my-0" text="Get Started"/></Link>
            <Button className="bg-black hover:bg-lightblack" text="Learn More"/>
        </div>
        </div>
    )
}   