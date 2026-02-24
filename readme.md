# Manuel d'installation & d'utilisation du projet


## Structure du projet

gestionnaire-restaurant/
│
├── app/                            # Le package de l'application
│   ├── __init__.py                 # Application Factory (crée l'app Flask)
│   ├── models.py                   # Tables BDD (User, Dish, Order) [cite: 35, 60]
│   ├── extensions.py               # Extensions (db, login_manager, bcrypt)
│   │
│   ├── admin/                      # [BLUEPRINT] Tout pour le Restaurateur
│   │   ├── __init__.py
│   │   ├── routes.py               # Routes: /admin/dashboard, /admin/add-dish
│   │   ├── forms.py                # Formulaires: AjoutPlatForm (avec validation image)
│   │   └── utils.py                # Fonctions: save_picture(), generate_csv() 
│   │
│   ├── auth/                       # [BLUEPRINT] Tout pour la Connexion
│   │   ├── __init__.py
│   │   ├── routes.py               # Routes: /login, /register, /logout
│   │   └── forms.py                # Formulaires: LoginForm, RegistrationForm
│   │
│   ├── main/                       # [BLUEPRINT] Tout pour le Client (Public)
│   │   ├── __init__.py
│   │   ├── routes.py               # Routes: /, /menu, /cart, /profile
│   │   └── forms.py                # Formulaires: UpdateProfileForm, OrderForm
│   │
│   ├── static/                     # Fichiers publics
│   │   ├── css/
│   │   │   └── style.css           # Ton CSS Responsive [cite: 61]
│   │   ├── js/
│   │   │   └── main.js
│   │   ├── img/                    # Images fixes (Logo, background)
│   │   └── uploads/                # Images dynamiques des plats [cite: 50]
│   │       └── dishes/             # Sous-dossier pour organiser les plats
│   │
│   └── templates/                  # Vues HTML (Jinja2)
│       ├── base.html               # Layout (Nav, Footer, Flash Messages)
│       ├── macros.html            # Composants réutilisables (ex: affichage d'un champ form)
│       ├── admin/                  # Templates Admin
│       │   ├── dashboard.html      # Vue globale [cite: 52]
│       │   ├── dish_form.html      # Page Ajout/Modif plat (même fichier pour les 2)
│       │   └── export.html         # Page pour télécharger le CSV
│       ├── auth/                   # Templates Auth
│       │   ├── login.html
│       │   └── register.html       # Création de compte [cite: 47]
│       └── main/                   # Templates Client
│           ├── index.html          # Accueil [cite: 41]
│           ├── menu.html           # Liste des plats pour commander [cite: 43]
│           ├── cart.html           # Panier et validation commande
│           └── profile.html        # Gestion compte client [cite: 44]
│
├── instance/                       # Données locales (ignoré par Git)
│   └── restaurant.db               # Ta base de données SQLite
│
├── docs/                           # Documentation TPI [cite: 64]
│   ├── journal_travail.docx
│   ├── planification.xlsx
│   ├── rapport_projet.docx
│   └── manuel_utilisateur.pdf
│
├── .env                            # [SECRET] Clés API, Secret Key, URL DB
├── .gitignore                      # Liste des fichiers exclus (venv, .env, *.pyc)
├── config.py                       # Classe de configuration (charge le .env)
├── requirements.txt                # Liste des libs (Flask, Flask-WTF, SQLAlchemy...)
└── run.py                          # Lanceur du serveur de développement