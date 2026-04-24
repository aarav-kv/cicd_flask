
from .user import user_bp
from .auth import auth_bp
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "secret123"
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    return app