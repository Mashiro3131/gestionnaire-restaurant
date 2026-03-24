# # https://flask.palletsprojects.com/en/stable/tutorial/views/

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.auth import auth as auth_bp
from app import db
from app.models import User


"""

------ LOGIN ------

"""

@auth_bp.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        # Utilise la méthode check_password de ton modèle
        if user and user.check_password(password):
            login_user(user)
            flash(f'Ravi de vous revoir, {user.first_name} !', 'success')
            
            if user.role and user.role.name == 'admin':
                return redirect(url_for('admin.dashboard'))
            return redirect(url_for('main.index'))
        
        flash('Email ou mot de passe incorrect.', 'danger')
    
    return redirect(url_for('main.index'))


"""

------ REGISTER ------

"""

@auth_bp.route('/register', methods=['POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        # Extraction des données du formulaire
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password')
        phone = request.form.get('phone', '').strip()
        
        # On combine Code Postal et Ville dans le champ 'address' de ton modèle
        zip_code = request.form.get('zip_code', '').strip()
        city = request.form.get('city', '').strip()
        full_address = f"{zip_code} {city}".strip()

        # Vérification si l'utilisateur existe déjà
        if User.query.filter_by(email=email).first():
            flash('Cet email est déjà enregistré.', 'warning')
            return redirect(url_for('main.index'))
        
        # Génération de l'username pour ton modèle
        username_gen = f"{first_name.lower()}.{last_name.lower()}" if first_name else email.split('@')[0]

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            username=username_gen,
            email=email,
            phone=phone,
            address=full_address
        )
        # On définit le mot de passe (le hachage est géré par la méthode du modèle)
        new_user.set_password(password)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Inscription réussie !', 'success')
            login_user(new_user)
        except Exception as e:
            db.session.rollback()
            flash('Erreur lors de la création du compte.', 'danger')

    return redirect(url_for('main.index'))


"""

------ LOGOUT ------

"""

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('main.index'))
