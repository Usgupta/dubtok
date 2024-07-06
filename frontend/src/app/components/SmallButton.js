

export default function SmallButton(props){
    var className = '';
    if ("className" in props){
        var className = props.className;
    }
   
        return (
            <button className={`transition-all bg-black px-10 py-3 rounded-xl text-white font-medium ${className}`}>{props.text}</button>
        )

    
}