import SmallButton from "./SmallButton"
import VideoPreview from "./VideoPreview"

export default function PreviewPage({videoFile, resetPage}){
    return(
   <div className="w-[100%] h-[100%]">
    <h1 className="text-2xl  md:text-4xl font-poppins mb-5">
        Your Video is Ready!
    </h1>
    <VideoPreview videoFile ={videoFile} className="mx-auto my-0"/>
    <SmallButton className= "bg-red hover:bg-darkred mb-5 mt-5 mx-auto " text="Dub Another File!" onClick={resetPage}/>
    </div>)
}
