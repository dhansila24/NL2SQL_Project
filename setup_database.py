import sqlite3

# Create database
conn = sqlite3.connect("clinic.db")
cursor = conn.cursor()

# patients table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone TEXT,
    date_of_birth DATE,
    gender TEXT,
    city TEXT,
    registered_date DATE
)
""")

# doctors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    specialization TEXT,
    department TEXT,
    phone TEXT
)
""")

# appointments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    appointment_date DATETIME,
    status TEXT,
    notes TEXT
)
""")

# treatments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS treatments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    appointment_id INTEGER,
    treatment_name TEXT,
    cost REAL,
    duration_minutes INTEGER
)
""")

# invoices table
cursor.execute("""
CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    invoice_date DATE,
    total_amount REAL,
    paid_amount REAL,
    status TEXT
)
""")

conn.commit()


print("Database created successfully!") 
import random
from datetime import datetime, timedelta

# Insert Doctors
specializations = ["Dermatology", "Cardiology", "Orthopedics", "General", "Pediatrics"]

for i in range(15):
    cursor.execute("""
    INSERT INTO doctors (name, specialization, department, phone)
    VALUES (?, ?, ?, ?)
    """, (
        f"Doctor {i+1}",
        random.choice(specializations),
        "General Dept",
        "9876543210"
    ))

# Insert Patients
cities = ["Chennai", "Madurai", "Coimbatore", "Salem", "Trichy"]

for i in range(200):
    cursor.execute("""
    INSERT INTO patients (first_name, last_name, email, phone, date_of_birth, gender, city, registered_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        f"Name{i}",
        "Test",
        None,
        None,
        "1995-01-01",
        random.choice(["M", "F"]),
        random.choice(cities),
        "2024-01-01"
    ))

# Insert Appointments
statuses = ["Scheduled", "Completed", "Cancelled", "No-Show"]

for i in range(500):
    cursor.execute("""
    INSERT INTO appointments (patient_id, doctor_id, appointment_date, status, notes)
    VALUES (?, ?, ?, ?, ?)
    """, (
        random.randint(1, 200),
        random.randint(1, 15),
        datetime.now() - timedelta(days=random.randint(0, 365)),
        random.choice(statuses),
        None
    ))

# Insert Treatments
for i in range(350):
    cursor.execute("""
    INSERT INTO treatments (appointment_id, treatment_name, cost, duration_minutes)
    VALUES (?, ?, ?, ?)
    """, (
        random.randint(1, 500),
        "General Checkup",
        random.randint(100, 5000),
        random.randint(10, 60)
    ))

# Insert Invoices
invoice_status = ["Paid", "Pending", "Overdue"]

for i in range(300):
    total = random.randint(100, 5000)
    paid = random.randint(0, total)

    cursor.execute("""
    INSERT INTO invoices (patient_id, invoice_date, total_amount, paid_amount, status)
    VALUES (?, ?, ?, ?, ?)
    """, (
        random.randint(1, 200),
        datetime.now() - timedelta(days=random.randint(0, 365)),
        total,
        paid,
        random.choice(invoice_status)
    ))

print("Dummy data inserted successfully!")
conn.close()