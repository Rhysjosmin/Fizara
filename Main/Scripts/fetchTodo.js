function FetchTodo(USER) {
  // http://127.0.0.1:5000/UserDB
  fetch(`${SERVER_URL}/${USER}/Todo`)
    .then((response) => response.json())
    .then((data) => {
      for (let index = 0; index < data.length; index++) {
        let todo = document.getElementById("TodoList");
        let listItem = document.createElement("li");
        listItem.textContent = data[index];
        listItem.addEventListener("click", () => closeTodo(this));
        todo.appendChild(listItem);
      }
    });
}
function closeTodo(e) {
  // alert(e)
  console.log(e);
}
