const Appointments = document.getElementById('UpcomingAppointments')
appointment = document.getElementById('appointmentTemplate')
AppointmentsArray = []
let content = appointment.content.cloneNode(true)
function fetchAppointments(Doctor){
fetch(`http://127.0.0.1:5000/${Doctor}/Appointments`)
  .then((response) => response.json())
  .then((data) => {
    AppointmentsArray = data
  })
  .then(() => {



    for (let PersonName in AppointmentsArray) {

      content = appointment.content.cloneNode(true)

      content.getElementById('AppointmentName').innerText = PersonName
      content.getElementById('AppointmentReason').innerText = AppointmentsArray[PersonName]['Reason']
      content.getElementById('AppointmentDate').innerText = AppointmentsArray[PersonName]['Date']
      content.getElementById('AppointmentTime').innerText = AppointmentsArray[PersonName]['Time']
      Appointments.appendChild(content)
    }
  }
  )}