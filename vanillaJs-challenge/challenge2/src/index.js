// <⚠️ DONT DELETE THIS ⚠️>
//import "./styles.css";
// <⚠️ /DONT DELETE THIS ⚠️>

const body = document.querySelector("body");
const SKYBLUE="skyblue";
const PURPLE="purple";
const YELLOW="yellow";
function resize(){
    const width=window.innerWidth;
    if(width>=1500){
        body.className=YELLOW;
    }
    else if(width<1500 && width>=800){
        body.className=PURPLE;
    }
    else{
        body.className=SKYBLUE;
    }
}

function init(){
    window.addEventListener("resize",resize);
}
resize();
init();