

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
            <button onClick={onClick} className={`transition-all bg-black px-10 py-3 rounded-xl text-white font-medium ${className}`}>{props.text}</button>
        )

    
}