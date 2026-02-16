from flask import Flask

def create_app():
    # Point static folder to the root static directory for better Vercel handling
    app = Flask(__name__, static_folder='../static', static_url_path='/static')
    app.config['SECRET_KEY'] = 'diabetes-prediction-secret-key-2026'
    
    # Register Blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
