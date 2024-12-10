import os
from flask import Flask
from models import db
from routes import bp as routes_bp

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

# Register routes
app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
