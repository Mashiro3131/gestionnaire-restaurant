# Configuration de l'application
import os
from dotenv import load_dotenv

load_dotenv() # Charger le .env

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')
    DEBUG = os.getenv('DEBUG') == 'True'
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')
    PORT = int(os.getenv('PORT', 5050))
    LANGUAGES = os.getenv('LANGUAGES', '').split(',')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False