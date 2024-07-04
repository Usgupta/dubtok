"use client";
import { useState } from "react";
import { Dropdown } from "flowbite-react";


export default function FormDrop() {
  const [selected, setSelected] = useState("Language");
  const customTheme = {
    root: {
      base: 'bg-white',
      inner: 'bg-white'
    }
  } 
  return (
    <Dropdown theme={{ floating: { target: "bg-white px-0 text-black w-30" } }} label={selected} dismissOnClick={false}>
      <Dropdown.Item onClick={() => setSelected("English")}>English</Dropdown.Item>
      <Dropdown.Item onClick={() => setSelected("Hindi")}>Hindi</Dropdown.Item>
      <Dropdown.Item onClick={() => setSelected("Chinese")}>Chinese</Dropdown.Item>
      <Dropdown.Item onClick={() => setSelected("Malay")}>Malay</Dropdown.Item>
    </Dropdown> 
  );
}