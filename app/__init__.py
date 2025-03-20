from flask import Flask
from app.blueprint.mechanics import mechanics_bp
from app.blueprint.service_tickets import service_ticket_bp
from .extensions import db, ma

def create_app(config_name="development"):
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(f'config.{config_name}')
    app.config['DEBUG'] = True

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    # Register blueprints
    app.register_blueprint(mechanics_bp, url_prefix='/mechanics')
    app.register_blueprint(service_ticket_bp, url_prefix='/service-tickets')

    return app
