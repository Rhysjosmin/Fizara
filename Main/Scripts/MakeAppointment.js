function MakeAppointment() {
  const issue = document.getElementById('DescribedIssue')
  
  let message=issue.value
  let doctorName=SelectedDoctor
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
      console.log('Message sent successfully!');
    })
    .catch(error => {
      console.error('There was a problem sending the message:', error);
    });
  }