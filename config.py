# Configuration de l'application

import os
from dotenv import load_dotenv

load_dotenv() # Charger

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')
    DEBUG = os.getenv('DEBUG') == 'True'
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
    PORT = int(os.getenv('PORT', 5050))
    