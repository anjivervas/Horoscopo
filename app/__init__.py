from flask import Flask
from flask_migrate import Migrate
from app.routes import main_bp
from app.settings import Config
from app.database import init_db, db
from app.extensions import register_error_handlers

def create_app():
    app = Flask(
        __name__,
        template_folder = 'templates')
    
    app.config.from_object(Config)
    init_db(app)
    Migrate(app, db)
    app.register_blueprint (main_bp)
    register_error_handlers(app)

    with app.app_context():
        print("Creando la base de datos...")
        db.create_all()

    return app