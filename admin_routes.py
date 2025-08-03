from flask import Blueprint, render_template, send_file, Response
import csv
import io
from fpdf import FPDF
from db import mongo

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/dashboard')
def admin_dashboard():
    appointments = mongo.db.appointments.find()
    users = mongo.db.users.find()
    return render_template('admin_dashboard.html', appointments=appointments, users=users)

@admin_bp.route('/admin/export/appointments/csv')
def export_appointments_csv():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Patient Name', 'Doctor', 'Date', 'Time', 'Status'])

    appointments = mongo.db.appointments.find()
    for appt in appointments:
        writer.writerow([appt.get('name'), appt.get('doctor'), appt.get('date'), appt.get('time'), appt.get('status')])

    output.seek(0)
    return Response(output, mimetype='text/csv', headers={"Content-Disposition":"attachment;filename=appointments.csv"})

@admin_bp.route('/admin/export/appointments/pdf')
def export_appointments_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Appointment Report", ln=True, align='C')
    pdf.ln(10)

    appointments = mongo.db.appointments.find()
    for appt in appointments:
        line = f"Name: {appt.get('name')} | Doctor: {appt.get('doctor')} | Date: {appt.get('date')} | Time: {appt.get('time')} | Status: {appt.get('status')}"
        pdf.multi_cell(0, 10, line)

    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    return send_file(pdf_output, as_attachment=True, download_name="appointments.pdf", mimetype='application/pdf')
