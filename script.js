const c1=document.createElement('div')

c1.id='c1'


document.body.append(c1)

const cursor1=document.getElementById('c1')

window.onmousemove=(e)=>{
    mX=e.clientX
    mY=e.clientY
    cursor1.style.transform=`translate3d(${mX-cursor1.clientWidth/2}px,${mY - cursor1.clientHeight}px,0)`
  
}




