import SmallButton from "./SmallButton"
import VideoPreview from "./VideoPreview"

export default function PreviewPage({videoFile, resetPage}){
    return(
   <div className="h-[450px]">
    <h1 className="text-2xl  md:text-4xl font-poppins mb-10">
        Your Video is Ready!
    </h1>
    <VideoPreview videoFile ={videoFile}/>
    <SmallButton className= "bg-red hover:bg-darkred mb-5 mt-5 ml-auto" text="Dub Another File!" onClick={resetPage}/>
    </div>)
}
