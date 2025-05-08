from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Basic config (optional: import from config.py)
    app.config['SECRET_KEY'] = 'super-secret-key-CHANGE-ME'

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    return app
