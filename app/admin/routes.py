from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from app.admin import admin

@admin.route('/dashboard')
def show_dashboard():
    try:
        # dashboard et dish_form.html 
        return render_template('admin/dashboard.html', title='Admin Dashboard')
    
    except TemplateNotFound:
        abort(404)