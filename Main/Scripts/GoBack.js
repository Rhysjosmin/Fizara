const body =document.body

 const button = document.createElement('button')

button.addEventListener('click',()=>{
    window.history.back()
})
button.innerText='Go Back'
button.style.position='fixed'
button.style.bottom='10px'
button.style.fontSize='1.4em'
button.style.padding='8px'
button.style.paddingInline='30px'

button.style.border='1px solid #10101066'
button.style.borderRadius='30px'

body.appendChild(button)