import React from "react";

export default function Button(props){
    var className = '';
    if ("className" in props){
        var className = props.className;
    }
   
        return (
            <button className={`transition-all w-[190px] h-[60px] lg:w-[250px] lg:whitespace-nowrap bg-black text-2xs px-1 md:px-3 lg:px-12 py-5 rounded-xl text-white font-medium ${className}`}>{props.text}</button>
        )

    
}