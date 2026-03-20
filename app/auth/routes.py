# # https://flask.palletsprojects.com/en/stable/tutorial/views/

# from flask import render_template, redirect, url_for, flash, request
# from app.auth import auth as auth_bp
# from app.auth.forms import LoginForm, RegisterForm
# from werkzeug.security import check_password_hash, generate_password_hash
# from app.models import User
# from flask_login import login_user, logout_user, current_user
# import instance


# @auth_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     """Route pour l'inscription d'un nouvel utilisateur."""
#     if current_user.is_authenticated:
#         return redirect(url_for('main.index')) # Redirige vers l'accueil si déjà connecté
    
#     form = RegisterForm()
#     if form.validate_on_submit():
#         # Hachage du mot de passe (ne JAMAIS stocker en clair)
#         hashed_pw = generate_password_hash(form.password.data)
        
#         user = User(
#             username=form.username.data,
#             email=form.email.data.lower(), # On stocke en minuscule par convention
#             password=hashed_pw
#         )
        
#         try:
#             db.session.add(user)
#             db.session.commit()
#             flash('Félicitations, vous êtes maintenant inscrit !', 'success')
#             return redirect(url_for('auth.login'))
#         except Exception as e:
#             db.session.rollback()
#             flash('Une erreur est survenue lors de l\'inscription.', 'danger')
            
#     return render_template('auth/register.html', title='Inscription', form=form)


# @auth_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     """Route pour la connexion des utilisateurs."""
#     if current_user.is_authenticated:
#         return redirect(url_for('main.index'))
    
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data.lower()).first()
        
#         # Vérification de l'existence et du mot de passe haché
#         if user and check_password_hash(user.password, form.password.data):
#             login_user(user)
            
#             # Gestion de la redirection "next" (si l'user venait d'une page protégée)
#             next_page = request.args.get('next')
#             flash(f'Ravi de vous revoir, {user.username} !', 'info')
#             return redirect(next_page) if next_page else redirect(url_for('main.index'))
#         else:
#             flash('Connexion échouée. Vérifiez vos identifiants.', 'danger')
            
#     return render_template('auth/login.html', title='Connexion', form=form)


# @auth_bp.route('/logout')

# @login_required
# def logout():
#     """Route pour la déconnexion."""
#     logout_user()
#     flash('Vous avez été déconnecté.', 'secondary')
#     return redirect(url_for('main.index'))


from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from app.models import User

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        # On utilise la méthode check_password de ton modèle
        if user and user.check_password(password):
            login_user(user) # Flask-Login gère la session tout seul
            flash('Bienvenue !', 'success')
            
            # Si c'est un admin (on vérifie via la relation backref 'role' de ton modèle)
            if user.role and user.role.name == 'admin':
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('index'))
        
        flash('Email ou mot de passe incorrect.', 'danger')
    return render_template('login.html')