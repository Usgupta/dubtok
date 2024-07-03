import React from "react";
import Button from "./Button";
import Link from 'next/link'
export default function MainDescription(){
    return (
        <div className="w-[693px] h-[300px] p-[20px]  flex flex-col justify-between">
            <h1 className="font-bold text-6xl">Diversify your content</h1>
            <p className="text-2xl">Dubtok empowers creators to reach a global audience by allowing their videos to be viewed in different languages</p>
        
        <div id="buttons" className="w-[400px]  flex flex-row justify-between">
        <Link href="/demo"><Button className="bg-red hover:bg-darkred" text="Get Started"/></Link>
        <Button className="bg-black hover:bg-lightblack" text="Learn More"/>
        </div>
        </div>
    )
}   