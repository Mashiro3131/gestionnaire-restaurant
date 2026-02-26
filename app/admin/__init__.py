from flask import Blueprint
auth = Blueprint('admin', __name__)
from app.admin import routes