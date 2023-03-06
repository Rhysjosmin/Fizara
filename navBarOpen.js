const menuButton= document.getElementById('menuButton')
const menu=document.getElementById('menu')
let state=true
if(window.innerWidth>500){
    menu.style.height='auto';
    menu.style.opacity=1
}else{
    menu.style.height='0';
    menu.style.opacity=0
}

window.onresize=e=>{
    // console.log(window.innerWidth)
    if(window.innerWidth>500){
        menu.style.height='auto';
        menu.style.opacity=1
    }else{
        menu.style.height='0';
        menu.style.opacity=0
    }
  

}
menuButton.onclick=()=>{
    state=!state;
    console.log(state)
    if(state){
        menu.style.height=0;
        menu.style.opacity=0

    }else{
        menu.style.opacity=1

        menu.style.height='auto';

    }
}
