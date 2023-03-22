let stars = [];
stars[0] = document.getElementById("star0");
stars[1] = document.getElementById("star1");
stars[2] = document.getElementById("star2");
stars[3] = document.getElementById("star3");
stars[4] = document.getElementById("star4");
// 0" onmouseleave="derate(0)" onmouseover="hoverRate(0)" onclick="setRate(0)"
function hoverRate(value) {
  if (stars[0].dataset.rating == "Unset") {
    for (let index = 0; index < stars.length; index++) {
      if (index <= value) {
        stars[index].classList.add("activeStar");
      } else {
        stars[index].classList.remove("activeStar");
      }
    }
  }
}
function setRate(value) {
  if (stars[0].dataset.rating != "Unset") {
    stars[0].dataset.rating = "Unset";
    console.log("unset");
  } else {
    for (let index = 0; index < stars.length; index++) {
      if (index <= value) {
        stars[index].classList.add("activeStar");
        stars[0].dataset.rating = value;
      } else {
        stars[index].classList.remove("activeStar");
      }
    }
  }
}
function derate(value) {
  if (stars[0].dataset.rating == "Unset") {
    stars.forEach((element) => {
      element.classList.remove("activeStar");
    });
  }
}
