# 🏥 Medicare Appointment & Prescription System

A web-based medical appointment booking and prescription management system built with **Flask** and **MongoDB**. This system allows patients to book appointments, doctors to upload prescriptions, and includes email reminders, secure login, and admin reporting features.

---

## 🚀 Features

- 👤 User Registration & Login (Patient/Doctor/Admin)
- 📅 Online Appointment Booking
- 🧾 Digital Prescription Upload (PDF/Text)
- ⏰ Email Reminders for Upcoming Appointments
- 📜 Prescription History Viewer
- 📊 Admin Dashboard with Report Generation (CSV/PDF)

---

## 🛠️ Tech Stack

| Layer        | Technology               |
|--------------|---------------------------|
| Frontend     | HTML, CSS, Bootstrap, JS |
| Backend      | Python (Flask Framework) |
| Database     | MongoDB (with PyMongo)   |
| Mail Service | Flask-Mail (SMTP)        |

---

## 🗂️ Project Folder Structure

```bash
Medicare_App2/
│
├── app.py                    # Main Flask App Initialization
├── db.py                     # MongoDB Connection Setup
├── requirements.txt          # Required Python Packages
├── static/                   # Static Assets (CSS, JS, Images)
├── templates/                # HTML Templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── ...
│
├── auth_routes.py            # User Authentication Logic
├── appointment_routes.py     # Appointment Booking Routes
├── prescription_routes.py    # Upload/View Prescriptions
├── reminder_routes.py        # Email Reminder Logic
├── admin_routes.py           # Admin Panel & Report Exports
│
└── utils/                    # Optional utility modules
    └── email_helper.py


📦 Installation

Clone the repository
-git clone https://github.com/Hiteshdravid/Medicare_App_Updated.git
-cd Medicare_App_Updated


*Create a virtual environment (optional but recommended)

-python -m venv venv
-venv\Scripts\activate  # On Windows


*Install required packages

pip install -r requirements.txt


Run the app
python app.py

👤 Author
Hitesh Dravid
📧 hiteshdravid@email.com

⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details.


