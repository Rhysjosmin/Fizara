const Nav = document.querySelector("aside").children[0].children;

NavArray = [
  "Dashboard",
  "Book an Appointment",
  "Diseases",
  "Maternal Health Issues",
  "Mental Health Counselling",
];
window.addEventListener("load", () => {
  console.log(Nav.length);
  for (let index = 1; index < Nav.length; index++) {
    const element = Nav[index];
    console.log(element.querySelector("a").innerText);
  }
  Nav.style.width = "70px";
});
