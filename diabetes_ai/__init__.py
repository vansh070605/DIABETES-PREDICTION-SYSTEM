from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'diabetes-prediction-secret-key-2026'
    
    # Register Blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
