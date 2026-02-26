from flask import Blueprint
main = Blueprint('main', __name__) # Crée un blueprint pour les routes principales (main)
from app.main import routes # Importe les routes définies dans app/main/routes.py

