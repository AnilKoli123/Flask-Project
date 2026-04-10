from flask import Blueprint, render_template, request, redirect
from app.models import Student, db
from flask_login import login_required

students = Blueprint('students', __name__)

@students.route('/students', methods=['GET', 'POST'])
@login_required
def manage_students():
    if request.method == 'POST':
        name = request.form['name']
        s = Student(name=name)
        db.session.add(s)
        db.session.commit()
        return redirect('/students')

    data = Student.query.all()
    return render_template('students.html', data=data)

@students.route('/delete_student/<int:id>')
def delete_student(id):
    s = Student.query.get(id)
    db.session.delete(s)
    db.session.commit()
    return redirect('/students')