from flask import Blueprint
auth = Blueprint('main', __name__)
from app.auth import routes

