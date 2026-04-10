from app import create_app
from app.models import db

app = create_app()

# Create DB tables
with app.app_context():
    db.create_all()

# Local run only
if __name__ == "__main__":
    app.run()
