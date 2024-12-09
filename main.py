import os
"""
Entry point for the Flask application.
"""

from flask import Flask
from routes import bp as routes_bp

app = Flask(__name__)

# Register the routes
app.register_blueprint(routes_bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
