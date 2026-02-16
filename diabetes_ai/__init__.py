import os
from flask import Flask

def create_app():
    # Use absolute path for static folder to be safe across different environments
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(base_dir, 'static')
    
    app = Flask(__name__, static_folder=static_dir, static_url_path='/static')
    app.config['SECRET_KEY'] = 'diabetes-prediction-secret-key-2026'
    
    # Register Blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
