from flask import Blueprint
auth = Blueprint('admin', __name__) # Change 'auth' par 'main' ou 'admin' selon le dossier
from app.auth import routes