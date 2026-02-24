# Crée l'application Flask et configure les routes, les modèles de données, etc.

from flask import Flask
from config import Config

def create_app():
    pass
    # app = Flask(__name__)
    # app.config.from_object(Config)
    # # Importer les routes
    # from app.auth import auth as auth_blueprint
    # from app.main import auth as main_blueprint
    # from app.admin import auth as admin_blueprint
    
    # app.register_blueprint(auth_blueprint)
    # app.register_blueprint(main_blueprint)
    # app.register_blueprint(admin_blueprint)
    
    # return app

