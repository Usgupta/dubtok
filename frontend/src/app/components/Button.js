import React from "react";

export default function Button(props){
    var className = '';
    if ("className" in props){
        var className = props.className;
    }
   
        return (
            <button className={`bg-black px-12 py-6 rounded-xl text-white font-medium ${className}`}>{props.text}</button>
        )

    
}