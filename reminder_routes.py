from flask import Blueprint
from datetime import datetime, timedelta
import threading
import time
import smtplib
from email.mime.text import MIMEText

reminder_bp = Blueprint('reminder', __name__)

def schedule_email_reminder(appointment):
    def send_email_later():
        try:
            # Combine date and time into a datetime object
            appt_datetime = datetime.strptime(f"{appointment['date']} {appointment['time']}", "%Y-%m-%d %H:%M")
            reminder_time = appt_datetime - timedelta(minutes=30)
            delay = (reminder_time - datetime.now()).total_seconds()

            print(f"[Reminder] Scheduled in {delay:.2f} seconds.")

            if delay > 0:
                time.sleep(delay)

            subject = "Appointment Reminder"
            message = f"""
            Dear {appointment['name']},

            This is a reminder for your appointment with Dr. {appointment['doctor']} at {appointment['time']} on {appointment['date']}.

            Reason: {appointment['reason']}

            Regards,
            Medicare Team
            """
            send_email(appointment['email'], subject, message)

        except Exception as e:
            print(f"[Reminder Error] {e}")

    threading.Thread(target=send_email_later).start()

def send_email(to_email, subject, message):
    try:
        # Replace these with your Gmail credentials
        sender_email = "dravidchellamuthu@gmail.com"
        sender_password = "eghw xhqz eemu rmbn"

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = to_email

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()

        print(f"[Email Sent] To: {to_email}")

    except Exception as e:
        print(f"[Email Error] {e}")
