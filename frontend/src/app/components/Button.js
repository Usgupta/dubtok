import React from "react";

export default function Button(props){
    var className = '';
    var onClick = ''
    if ("className" in props){
        var className = props.className;
    }
    if ("onClick" in props){
        var onClick = props.onClick
    }
   
        return (
            <button className={`transition-all bg-black px-12 py-6 rounded-xl text-white font-medium ${className}`} onClick={onClick}>{props.text}</button>
        )

    
}