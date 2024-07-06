import VideoPreview from "./VideoPreview"

export default function PreviewPage({videoFile}){
    return(
   <div className={"h-[500px] w-[700px] p-10 mr-3 border-black border-2 bg-lightgrey border-black border-2 drop-shadow-xl rounded-[18px] flex flex-col items-center justify-start"}>
    <h1 className="text-4xl font-poppins mb-10">
        Your Video is Ready!
    </h1>
    <VideoPreview videoFile ={videoFile}/>
    </div>)
}