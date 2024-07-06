import React from "react";
import Button from "./Button";
import Link from 'next/link'
export default function MainDescription({className}){
    return (
        <div id="mainDescription" className={`w-[200px] lg:w-[705px] h-[40vh] p-[20px]  flex flex-col justify-between mr-6 ${className}`}>
            <h1 className="font-bold text-xl lg:text-6xl">Diversify your content</h1>
            <p className=" text-sm lg:text-2xl">Dubtok empowers creators to reach a global audience by allowing their videos to be viewed in different languages</p>
        
        < div id="buttons" className="w-[200px] md:w-[400px] flex flex-col lg:flex-row justify-between">
            <Link href="/demo"><Button className="bg-red hover:bg-darkred my-2  lg:mr-2 lg:my-0" text="Get Started"/></Link>
            <Button className="bg-black hover:bg-lightblack" text="Learn More"/>
        </div>
        </div>
    )
}   