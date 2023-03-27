const menuButton= document.getElementById('menuButton')
const menu=document.getElementById('menu')
window.dispatchEvent(new Event('resize'));
let state=true
menuButton.textContent='menu'

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
    console.log(state)

    state=!state;
    console.log(state)
    if(state){
        menuButton.textContent='menu'

        menu.style.height=0;
        menu.style.opacity=0

    }else{
        menuButton.textContent='close'
        menu.style.opacity=1
        menu.style.height='auto';

    }
}
