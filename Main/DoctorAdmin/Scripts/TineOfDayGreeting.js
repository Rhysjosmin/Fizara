function ToD(){
var currentTime = new Date();
currentTime.getHours();
var currentHour = currentTime.getHours();
const TimeOfDayDisplay = document.getElementById("TimeOfDay");
switch (true) {
    case currentHour < 12:
        TimeOfDayDisplay.innerText = "Good Morning!";
        break;
    case currentHour > 12 && currentHour < 17:
        TimeOfDayDisplay.innerText = "Good Afternoon!";

        break;
    default:
        TimeOfDayDisplay.innerText = "Good Evening!";

        break;
}
}
