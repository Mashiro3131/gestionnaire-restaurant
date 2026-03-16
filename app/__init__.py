"""
Crée le backbone du projet Flask en configurant les routes, les modèles de données, etc.
"""

from flask import Flask,request, g 
from app.extensions import db, login_manager, babel
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialiser les extensions
    db.init_app(app)
    login_manager.init_app(app)
    babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)

    app.route("/")(lambda: "Hello, World!")  # Route de test pour vérifier que l'app fonctionne

    """ Importer les routes """
    # Main Blueprint
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    # Admin Blueprint
    from app.admin import admin as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    # Authentication Blueprint
    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone

def get_locale():
    if not g.get('lang_code', None):
        g.lang_code = request.accept_languages.best_match(Config.LANGUAGES)
    return g.lang_code
    # https://medium.com/@ishanthari96/create-a-multilingual-web-application-using-python-flask-babel-2e4a36471dc3