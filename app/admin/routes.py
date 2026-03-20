from flask import render_template, abort
from jinja2 import TemplateNotFound
from app.admin import admin
from app.models import Dish


@admin.route('/admin')
# @login_required
def admin_dashboard():
    # CRUD Plats
    dishes = Dish.query.all()
    return render_template('admin/dashboard.html', dishes=dishes)


@admin.route('/dashboard')
def show_dashboard():
    try:
        # dashboard et dish_form.html 
        return render_template('admin/dashboard.html', title='Admin Dashboard')
    
    except TemplateNotFound:
        abort(404)