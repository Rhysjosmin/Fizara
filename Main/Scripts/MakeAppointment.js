function MakeAppointment_Outer() {
  if (
    document.getElementById("DescribedIssue").value.replace(" ", "") !=
    "" &&
    SelectedDoctor.replace(" ", "") != "" &&
    document.getElementById("dateTime").value.replace(" ", "") !=
    "" 
  ) {
    MakeAppointment();
  } else {
    alert2("Incomplete Form", "Please Fill All the Fields");
  }
}
function MakeAppointment() {
  const issue = document.getElementById('DescribedIssue')
  const dateTime=document.getElementById('dateTime')

  
  let message=issue.value
  let doctorName=SelectedDoctor.replace('Dr. ','')
  fetch(`${SERVER_URL}/MakeAppointment`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        message: message,
        doctor_name: doctorName,
        user_name: USER,
        date:dateTime.value
      })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      jsConfetti.addConfetti()
      setTimeout(()=>{
        window.location.replace("./index.html?User=" + USER);
      },1000) 

      console.log('Message sent successfully!');
    })
    .catch(error => {
      console.error('There was a problem sending the message:', error);
    });
  }