function FetchTodo(USER){
    fetch(`${SERVER_URL}/${USER}/Todo`)
    .then((response) => response.json())
    .then((data) => {
        // console.log(data.length)
        for (let index = 0; index < data.length; index++) {
            
            let todo =document.getElementById('TodoList')
            let listItem=document.createElement('li')
            listItem.textContent=data[index]
            listItem.addEventListener('click',()=>closeTodo(this))
            todo.appendChild(listItem)
        }
    })

}
function closeTodo(e){
// alert(e)
console.log(e)
}