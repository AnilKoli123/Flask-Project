from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Student, Subject, Attendance

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def home():
    return render_template('dashboard.html',
        students=Student.query.count(),
        subjects=Subject.query.count(),
        attendance=Attendance.query.count()
    )