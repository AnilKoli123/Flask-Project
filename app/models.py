from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# ---------------- USER ----------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.String(20))  # admin, teacher, student

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

# ---------------- STUDENT ----------------
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# ---------------- SUBJECT ----------------
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    teacher_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# ---------------- ATTENDANCE ----------------
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    subject_id = db.Column(db.Integer)
    date = db.Column(db.String(20))
    status = db.Column(db.String(10))  # Present / Absent

# ---------------- ASSIGNMENT ----------------
class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    subject_id = db.Column(db.Integer)
    file = db.Column(db.String(200))

# ---------------- SUBMISSION ----------------
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer)
    student_id = db.Column(db.Integer)
    file = db.Column(db.String(200))