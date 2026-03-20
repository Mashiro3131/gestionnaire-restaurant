from flask import render_template, abort
from app.main import main as main_bp
from app.models import *
from jinja2 import TemplateNotFound
#from flask_babel import gettext as _
# https://realpython.com/flask-blueprint/#what-a-flask-application-looks-like



@main_bp.route('/')
def index():

    # dishes = Dish.query.filter_by(is_active=True).all()
    try:
        return render_template('main/index.html', title=('Home'))
    except TemplateNotFound:
        abort(404)



@main_bp.route('/menu')
def menu():
    dishes = Dish.query.all()
    return render_template('main/menu.html', dishes=dishes)


# Page Navbar Order
@main_bp.route('/order')
def order():
    order = Order.query.all()
    return render_template('main/order.html', order=order)

# Page Navbar Contact
@main_bp.route('/contact')
def contact():
    # Route simple pour la page de contact
    return render_template('main/contact.html')