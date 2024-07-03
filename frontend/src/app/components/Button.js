import React from "react";

export default function Button(props){

    if ("color" in props){
        return (
            <button className={`bg-${props.color} px-12 py-6 rounded-xl text-white font-medium`}>{props.text}</button>
        )
    }
        return (
            <button className="bg-black px-12 py-6 rounded-xl text-white font-medium">{props.text}</button>
        )

    
}