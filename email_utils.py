import smtplib
from email.message import EmailMessage

def send_appointment_email(appointment):
    sender_email = 'dravidchellamuthu@gmail.com'
    app_password = 'eghw xhqz eemu rmbn'  # replace with your real app password

    # 1. Email to Patient
    msg_patient = EmailMessage()
    msg_patient['Subject'] = 'Appointment Confirmation'
    msg_patient['From'] = sender_email
    msg_patient['To'] = appointment['email']
    msg_patient.set_content(f'''
    Hi {appointment['name']},

    Your appointment is confirmed.

    Date: {appointment['date']}
    Time: {appointment['time']}
    Doctor: {appointment['doctor']}
    Reason: {appointment['reason']}

    Please reach 10 minutes early.
    ''')

    # 2. Email to Doctor or Clinic
    msg_doctor = EmailMessage()
    msg_doctor['Subject'] = 'New Appointment Booked'
    msg_doctor['From'] = sender_email
    msg_doctor['To'] = appointment.get('doctor_email', 'clinic@example.com')  # fallback email
    msg_doctor.set_content(f'''
    A new appointment has been booked.

    Patient Name: {appointment['name']}
    Email: {appointment['email']}
    Date: {appointment['date']}
    Time: {appointment['time']}
    Reason: {appointment['reason']}
    ''')

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender_email, app_password)
            smtp.send_message(msg_patient)
            smtp.send_message(msg_doctor)
            print("✅ Emails sent to patient and doctor successfully.")
    except Exception as e:
        print("❌ Failed to send emails:", e)
