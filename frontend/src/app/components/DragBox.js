"use client";
import React from 'react'
import Dropzone from 'react-dropzone'

export default function DragBox() {
  
  return (<Dropzone onDrop={acceptedFiles => console.log(acceptedFiles)}>
  {({getRootProps, getInputProps}) => (
    <section >
      <div {...getRootProps()} className="border-black border-2 border-dotted w-60 h-40 bg-white">
        <input {...getInputProps()} />
        <p>Upload File</p>
      </div>
    </section>
  )}
</Dropzone>)
}


