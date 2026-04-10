import os
from flask import Blueprint, render_template, request, redirect
from werkzeug.utils import secure_filename
from app.models import Assignment, db
from flask_login import login_required

assignments = Blueprint('assignments', __name__)

UPLOAD_FOLDER = 'app/static/uploads'

@assignments.route('/assignments', methods=['GET','POST'])
@login_required
def manage_assignments():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        a = Assignment(
            title=request.form['title'],
            subject_id=request.form['subject'],
            file=filename
        )
        db.session.add(a)
        db.session.commit()

    return render_template('assignments.html',
        data=Assignment.query.all()
    )