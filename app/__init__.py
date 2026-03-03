# Crée l'application Flask et configure les routes, les modèles de données, etc.
from flask import Flask, g, request
from app.extensions import db, login_manager, babel
from config import Config

def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialiser les extensions
    db.init_app(app)
    login_manager.init_app(app)
    babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)

    # Importer les routes
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app

# Fonction pour déterminer la langue de l'utilisateur
def get_locale():
    # if a user is logged in, use the locale from the user settings
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support de/fr/en in this
    # example.  The best match wins.
    return request.accept_languages.best_match(['fr', 'de', 'en'])
