from flask import Blueprint, render_template, request, redirect
from app.models import Attendance, Student, Subject, db
from flask_login import login_required
from datetime import date

attendance = Blueprint('attendance', __name__)

@attendance.route('/attendance', methods=['GET','POST'])
@login_required
def mark_attendance():
    students = Student.query.all()
    subjects = Subject.query.all()

    if request.method == 'POST':
        for s in students:
            status = request.form.get(str(s.id))
            a = Attendance(
                student_id=s.id,
                subject_id=request.form['subject'],
                date=str(date.today()),
                status=status
            )
            db.session.add(a)
        db.session.commit()

    return render_template('attendance.html',
        students=students,
        subjects=subjects
    )