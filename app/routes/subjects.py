from flask import Blueprint, render_template, request, redirect
from app.models import Subject, User, db
from flask_login import login_required

subjects = Blueprint('subjects', __name__)

@subjects.route('/subjects', methods=['GET','POST'])
@login_required
def manage_subjects():
    teachers = User.query.filter_by(role='teacher').all()

    if request.method == 'POST':
        sub = Subject(
            name=request.form['name'],
            teacher_id=request.form['teacher']
        )
        db.session.add(sub)
        db.session.commit()

    return render_template('subjects.html',
        data=Subject.query.all(),
        teachers=teachers
    )