import React from "react";

export default function Button(props){
    var className = '';
    if ("className" in props){
        var className = props.className;
    }
   
        return (
            <button className={`transition-all  bg-black px-5 lg:px-12 py-3 lg:py-6 rounded-xl text-white font-medium ${className}`}>{props.text}</button>
        )

    
}