# Extensions (SQLAlchemy, LoginManager, etc.)

import colorama
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

colorama.init(autoreset=True)

#from flask_babel import Babel

db = SQLAlchemy()
login_manager = LoginManager()
# babel = Babel()