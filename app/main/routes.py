from app.main import main

@main.route('/')
def index():
    return "<h1>Bienvenue sur la page d'accueil du restaurant !</h1>"