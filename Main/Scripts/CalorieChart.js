
let OFFSET=0
let SIZE=20
function StartCalorieChart(USER,Start,End) {
  let value = 0;
  let size = 20;
  let count = 0;
  var xValues = new Array(size);
  var labels = new Array(size);
  labels.fill(0);
  xValues.fill(0);
//   xValues.fill(100, 200);
//   xValues.fill(-100, 220);
//   xValues.fill(0, 2);
  var CalorieChart = new Chart("CalorieChartID", {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "",
          lineTension: .4,      
          data: xValues,
          borderColor: "rgb(50, 115, 255)",
          fill: false,
        },
      ],
    },
    options: {
      scales: {
        xAxes: [
          {
            display: false,
          },
        ],
        yAxes: [
          {
            display: false,
          },
        ],
      },
      legend: {
        display: false,
      },

      animation: false,
      responsive: true,
    },
  });

  CalorieChart.data.datasets[0].pointRadius = 0;
  fetch(`${SERVER_URL}/UserDB`)
  .then((response)=>response.json())
  .then((data)=>{
    Calories=data[USER]['Calorie']
    // console.log(CalorieChart.data.datasets[0].data) 
    // console.log(Calories) 
    console.log(Calories.slice(Start,End)) 

    CalorieChart.data.datasets[0].data=Calories.slice(Start, End);

    CalorieChart.update()

  })
}

function sendCalorie() {
  OFFSET=OFFSET+1
  fetch(
    `${SERVER_URL}/AppendCalorie/${USER}/${
      document.getElementById("CalorieInput").value
    }`

  ).then(() => StartCalorieChart(USER,0+OFFSET,SIZE+OFFSET))
  .then(()=>{
    fetch(`${SERVER_URL}/${USER}/AverageCalorie`)
    .then((response)=>response.json())
    .then((data)=>{
      document.getElementById('CalorieAverage').innerText=data
    })
  }
  )
}

fetch(`${SERVER_URL}/${USER}/AverageCalorie`)
.then((response)=>response.json())
.then((data)=>{
  document.getElementById('CalorieAverage').innerText=data
})