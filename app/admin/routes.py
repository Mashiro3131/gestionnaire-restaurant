from flask import render_template, abort, url_for, redirect, flash
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound
from app.admin import admin as admin
from app.models import Dish


@admin.route('/admin')
@login_required 
def admin_dashboard():
    # Vérifie si le rôle lié à l'utilisateur est bien admin
    if not current_user.role or current_user.role.name != 'admin':
        flash("Accès réservé aux administrateurs.", "danger")
        return redirect(url_for('index'))
        
    dishes = Dish.query.all()
    return render_template('admin/dashboard.html', dishes=dishes)


@admin.route('/dashboard')
def show_dashboard():
    try:
        # dashboard et dish_form.html 
        return render_template('admin/dashboard.html', title='Admin Dashboard')
    
    except TemplateNotFound:
        abort(404)
        
        