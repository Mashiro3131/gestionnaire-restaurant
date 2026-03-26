# Gestionnaire de restaurant

## Description du projet

Ce projet est un gestionnaire de restaurant développé en Python avec le framework Flask. Il permet au restaurateur de gérer son menu, les commandes et les clients, tandis que les clients peuvent consulter le menu, passer des commandes et gérer leur profil.

# Iko's Restaurant

Projet réalisé dans le cadre de mon **TPI (Travail Pratique Individuel)** de fin de CFC d'Informaticien. 
L'objectif était de créer une application web complète, moderne et intuitive pour la gestion de commandes de repas.
Il permet au restaurateur de gérer son menu, les commandes et les clients, tandis que les clients peuvent consulter le menu, passer des commandes et gérer leur profil.

### Fonctionnalités Clés
* **Menu Dynamique** : Filtrage instantané par catégorie (Entrées, Plats, Desserts) sans rechargement de page.
* **Panier Offcanvas** : Système de panier persistant via session Flask, accessible depuis n'importe quelle page.
* **Authentification Sécurisée** : Gestion des utilisateurs (Login/Register) avec Flask-Login et protection des mots de passe (Hachage).
* **Finalisation de Commande** : Formulaire intégré au panier pour le choix de la date, de l'heure et de l'adresse de livraison.
* **Interface Admin** : Dashboard pour la gestion du catalogue de plats (CRUD) !!! NON IMPLÉMENTÉ !!!.

---

## Stack Technique
Pour ce projet, j'ai choisi des technologies robustes et modernes :

* **Backend** : Python 3.x avec le framework **Flask**.
* **Base de données** : **SQLite** avec l'ORM **SQLAlchemy** (Modèle relationnel).
* **Frontend** : **HTML5/CSS3**, **Bootstrap 5** (pour le responsive et les composants UI), et **JavaScript ES6**.
* **Templating** : **Jinja2** pour le rendu dynamique des données.

---

## Installation & Lancement

1. **Cloner le projet**
   ```bash
   git clone [https://github.com/ton-username/ikos-restaurant.git](https://github.com/ton-username/ikos-restaurant.git)
   cd ikos-restaurant

2. **Créer l'environnement virtuel**
```bash
python -m venv flask
source venv/Scripts/activate  
```
3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```
4. **Lancer l'application**
```bash
python run.py
```
5. **Resultat**
```bash
(flask) λ python run.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 415-005-036
```

## Sources

- [Flask Mega-Tutorial de Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)
- [User Authentication and Authorization in Flask](https://medium.com/@mathur.danduprolu/user-authentication-and-authorization-in-flask-building-secure-login-and-access-control-part-5-7-59679a08cdc3)
