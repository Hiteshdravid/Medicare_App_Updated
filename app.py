from flask import Flask
from db import mongo
from auth_routes import auth_bp
from appointment_routes import appointment_bp
from reminder_routes import reminder_bp
from prescription_routes import prescription_bp
from admin_routes import admin_bp  # Admin Panel
from flask import redirect, url_for
from email_utils import send_appointment_email



app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# MongoDB Config
app.config['MONGO_URI'] = 'mongodb://localhost:27017/medicare2'
mongo.init_app(app)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(appointment_bp)
app.register_blueprint(reminder_bp)
app.register_blueprint(prescription_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def home():
     return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
