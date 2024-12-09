from models import db
from main import app

with app.app_context():
    db.init_app(app)
    db.create_all()
    print("Database initialized successfully.")
