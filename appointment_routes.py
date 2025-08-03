from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from db import mongo
from bson.objectid import ObjectId
from email_utils import send_appointment_email
from reminder_routes import schedule_email_reminder

appointment_bp = Blueprint('appointment', __name__)

@appointment_bp.route('/book', methods=['GET', 'POST'])
def book_appointment():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        # Fetch user email from DB
        user = mongo.db.users.find_one({'_id': ObjectId(session['user_id'])})
        email = user.get('email', '') if user else ''

        appointment = {
            'user_id': session['user_id'],
            'name': request.form['name'],
            'doctor': request.form['doctor'],
            'doctor_email': request.form['doctor_email'],
            'date': request.form['date'],
            'time': request.form['time'],
            'reason': request.form['reason'],
            'email': email
        }

        mongo.db.appointments.insert_one(appointment)
        schedule_email_reminder(appointment)  # 🔔 Email reminder

          #Email notification to doctor
        send_appointment_email(appointment)


        flash('Appointment booked successfully!', 'success')
        return redirect(url_for('auth.dashboard'))

    return render_template('book_appointment.html')

@appointment_bp.route('/appointments')
def view_appointments():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    appointments = mongo.db.appointments.find({'user_id': session['user_id']})
    return render_template('view_appointments.html', appointments=appointments)
