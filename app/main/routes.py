from flask import render_template, abort, request, flash, redirect, url_for, session
from flask_login import login_required, current_user
from app.main import main as main_bp
from app.models import Dish, Order, OrderItem
from app import db
from datetime import datetime
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


@main_bp.app_context_processor
def inject_dish_lookup():
    def get_dish_by_id(dish_id):
        return Dish.query.get(int(dish_id))
    return dict(get_dish_by_id=get_dish_by_id)


@main_bp.route('/menu')
def menu():
    try:
        all_dishes = Dish.query.filter_by(is_active=True).all()
        return render_template('main/menu.html', dishes=all_dishes)
    except TemplateNotFound:
            abort(404)


@main_bp.route('/order', methods=['GET', 'POST'])
@login_required
def order():
    # Traitement de la commande 
    if request.method == 'POST':
        dish_id = request.form.get('dish_id')
        dish = Dish.query.get_or_404(dish_id)
        
        delivery_date_str = request.form.get('delivery_date')
        delivery_time_str = request.form.get('delivery_time')
        address = request.form.get('address')
        quantity = int(request.form.get('quantity', 1))
        
        try:
            full_delivery_dt = datetime.strptime(f"{delivery_date_str} {delivery_time_str}", '%Y-%m-%d %H:%M')
            
            new_order = Order(
                user_id=current_user.id,
                delivery_date=full_delivery_dt,
                delivery_address=address,
                total_price=dish.price * quantity,
                status="en attente"
            )
            
            item = OrderItem(dish_id=dish.id, quantity=quantity, unit_price=dish.price)
            new_order.order_items.append(item)
            
            db.session.add(new_order)
            db.session.commit()
            
            flash('Commande validée ! Bon appétit.', 'success')
            return redirect(url_for('main.index'))
            
        except ValueError:
            flash("Format de date ou heure invalide.", "danger")
            return redirect(url_for('main.order'))

    all_dishes = Dish.query.filter_by(is_active=True).all()
    return render_template('main/order.html', dishes=all_dishes, now=datetime.now())


# Page Navbar Contact
@main_bp.route('/contact')
def contact():
    
    return render_template('main/contact.html')


