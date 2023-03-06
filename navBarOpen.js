const menuButton= document.getElementById('menuButton')
const menu=document.getElementById('menu')
let state=false

window.onresize=()=>{
    menu.style.height='auto';
    menu.style.opacity=1

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
