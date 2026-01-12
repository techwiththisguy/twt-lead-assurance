from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Basic config (Expand Later)
    app.config["SECRET_KEY"] = "dev-secret-change-me"
    
    # Register routes
    from .routes_public import public_bp
    app.register_blueprint(public_bp)
    
    return app