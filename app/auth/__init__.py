from flask import Blueprint
auth_bp = Blueprint('auth', __name__) # Change 'auth' par 'main' ou 'admin' selon le dossier
from app.auth import routes