from flask import Blueprint
auth = Blueprint('admin', __name__)
from app.auth import routes