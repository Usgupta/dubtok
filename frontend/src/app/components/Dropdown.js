"use client";
import { useState } from "react";
import { Dropdown } from "flowbite-react";


export default function FormDrop({setDub}) {
  function setOption(s){
    setSelected(s);
    setDub(s)
  }
  const [selected, setSelected] = useState("Language");
  const customTheme = {
    root: {
      base: 'bg-white',
      inner: 'bg-white'
    }
  } 
  return (
    <Dropdown  theme={{ floating: { target: "hover:bg-lightgrey bg-white px-0 py-0 text-xs text-black w-24 md:w-32"} }} label={selected} dismissOnClick={false}>
      <Dropdown.Item onClick={() => setOption("English")}>English</Dropdown.Item>
      <Dropdown.Item onClick={() => setOption("French")}>French</Dropdown.Item>
      <Dropdown.Item onClick={() => setOption("Chinese")}>Chinese</Dropdown.Item>
      <Dropdown.Item onClick={() => setOption("Malay")}>Malay</Dropdown.Item>
    </Dropdown> 
  );
}