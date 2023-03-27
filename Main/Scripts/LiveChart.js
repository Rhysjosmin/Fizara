function StartChart(){

let value=0
let size=500
let count=0
var xValues = new Array(size);
var labels = new Array(size);
labels.fill(0)
xValues.fill(0)
xValues.fill(100,200)
xValues.fill(-100,220)
xValues.fill(0,2)
var heartRate=new Chart("myChart", {
  type: "line",
  data: {
  
    labels: labels,
    datasets: [{ 
      label:'',
      data: xValues,
      borderColor: "rgb(50, 115, 255)",
      fill: false,

    }]
  },
  options: {

scales:{
  xAxes:[{
    display: false
  }],
  yAxes:[{
    display: false
  }],
},
    legend: {
      display: false
  },


    animation:false,
    responsive: true
  }
});
sin=Math.sin
cos=Math.cos
heartRate.data.datasets[0].pointRadius = 0;
setInterval(()=>{

  heartRate.data.datasets.forEach((dataset) => {
    count+=.1
    for (let index = 0; index <8; index++) {
      n=index
      x=count
      value=((sin(n*x)*-0.1)*Math.random()*4)+value
      // value=Math.sin(index*count)*0.1-value
      
    }
    
    value=Math.round(value)
    dataset.data.push(value);
 heartRate.update()

    if(dataset.data.length>size){
      dataset.data.shift();
    }
 });
 heartRate.update()
},50)
}