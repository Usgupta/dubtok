

export default function SmallButton(props){
    let className = '';
    if ("className" in props){
        className = props.className;
    }

    let onClick = () =>{
        return
    };
    if ("onClick" in props){
        onClick = props.onClick
    }
   
        return (
            <button onClick={onClick} className={`transition-all text-xs lg:text-md bg-black px-5 lg: px-10 py-2 lg:py-3 rounded-xl text-white font-medium ${className}`}>{props.text}</button>
        )

    
}