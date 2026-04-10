from flask import Blueprint, render_template, request, redirect
from app.models import User, db
from flask_login import login_user, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect('/dashboard')
    return render_template('login.html')   # ✅ FIXED

@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user = User(
            name=request.form['name'],
            email=request.form['email'],
            role=request.form['role']
        )
        user.set_password(request.form['password'])
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('register.html')   # ✅ FIXED

@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/')