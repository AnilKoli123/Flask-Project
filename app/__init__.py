from flask import Flask
from .models import db, User
from flask_login import LoginManager

login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder='templates')

    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    db.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes.auth import auth
    from .routes.dashboard import dashboard
    from .routes.students import students
    from .routes.subjects import subjects
    from .routes.attendance import attendance
    from .routes.assignments import assignments

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(students)
    app.register_blueprint(subjects)
    app.register_blueprint(attendance)
    app.register_blueprint(assignments)

    return app