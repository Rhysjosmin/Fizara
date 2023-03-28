function MakeAppointment_Outer() {
  if (
    document.getElementById("DescribedIssue").value.replace(" ", "") !=
    "" &&
    SelectedDoctor.replace(" ", "") != ""
  ) {
    MakeAppointment();
  } else {
    alert2("Incomplete Form", "Please Fill All the Fields");
  }
}
function MakeAppointment() {
  const issue = document.getElementById('DescribedIssue')
  
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
        user_name: USER
      })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      // window.location.replace("./index.html?User=" + USER);

      console.log('Message sent successfully!');
    })
    .catch(error => {
      console.error('There was a problem sending the message:', error);
    });
  }