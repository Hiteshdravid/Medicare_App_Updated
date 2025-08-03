from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from db import mongo

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = generate_password_hash(request.form['password'])


        existing_user = mongo.db.users.find_one({'email': email})
        if existing_user:
            flash("Email already registered.", 'danger')
        else:
            mongo.db.users.insert_one({'email': email, 'password': password})
            flash("Registration successful!", 'success')
            return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = mongo.db.users.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            flash('Login successful', 'success')
            return redirect(url_for('auth.dashboard'))
        flash("Invalid credentials", 'danger')
    return render_template('login.html')

@auth_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully", 'info')
    return redirect(url_for('auth.login'))
