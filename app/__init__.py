# Crée l'application Flask et configure les routes, les modèles de données, etc.


from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Importer les routes
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

