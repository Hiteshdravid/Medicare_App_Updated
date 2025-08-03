from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from db import mongo
from bson.objectid import ObjectId
import datetime

prescription_bp = Blueprint('prescription', __name__)

@prescription_bp.route('/upload_prescription', methods=['GET', 'POST'])
def upload_prescription():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        prescription = {
            'user_id': session['user_id'],
            'doctor': request.form['doctor'],
            'date': request.form['date'],
            'notes': request.form['notes'],
            'medications': request.form['medications']
        }
        mongo.db.prescriptions.insert_one(prescription)
        flash('Prescription uploaded successfully!', 'success')
        return redirect(url_for('prescription.view_prescriptions'))

    return render_template('upload_prescription.html')

@prescription_bp.route('/prescriptions')
def view_prescriptions():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    prescriptions = mongo.db.prescriptions.find({'user_id': session['user_id']})
    return render_template('view_prescriptions.html', prescriptions=prescriptions)
