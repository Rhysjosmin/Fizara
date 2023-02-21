// const c1=document.createElement('div')
// c1.id='c1'

// document.body.append(c1)
const cursor1=document.getElementById('cursor0')

window.onmousemove=(e)=>{
console.log(e.clientX)
console.log(e.clientY)
mX=e.clientX- cursor1.clientWidth/2
mY=e.clientY-cursor1.clientHeight/2
cursor1.style.transform=`translate3d(${mX}px,${mY}px,0)`

}



