import React from "react";

export default function Button(props){
    return (
        <button className="bg-red px-20 py-15 rounded-xl text-white">{props.text}</button>
    )
}