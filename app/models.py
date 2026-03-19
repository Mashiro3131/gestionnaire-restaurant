"""
Fichier pour les modèles de données de l'application (une sorte de phpmyadmin manuel pour sqlite). 
Ici, on définit les classes qui représentent les tables de la base de données et leurs relations.
Tables BDD (User, Dish, Order, OrderItem, Role)
"""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, Numeric, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from app.extensions import db, login_manager


# --- CALLBACK POUR FLASK-LOGIN ---
@login_manager.user_loader
def load_user(user_id):
    # Flask-Login utilise l'ID pour retrouver l'utilisateur en session
    return User.query.get(user_id)

# --- IAM : ROLES ---
class Role(db.Model):
    __tablename__ = "roles"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(50), nullable=False, unique=True)

    users = relationship("User", backref="role", lazy=True)

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)

# --- UTILISATEURS ---
class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(80), unique=True)
    email = Column(String(254), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    phone = Column(String(20))
    address = Column(Text)
    preferred_payment_method = Column(String(50))
    role_id = Column(String(36), ForeignKey("roles.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship("Order", backref="customer", lazy=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return f"<User {self.email}>"

# --- MENU (LES PLATS) ---
class Dish(db.Model):
    __tablename__ = "dishes"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(120), nullable=False)
    category = Column(String(50))
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    image_url = Column(String(500))
    is_active = Column(Boolean, default=True)
    max_daily_quantity = Column(Integer, default=20)

    order_items = relationship("OrderItem", backref="dish", lazy=True)

    def __init__(self, **kwargs):
        super(Dish, self).__init__(**kwargs)

    def __repr__(self):
        return f"<Dish {self.name}>"

# --- COMMANDES ---
class Order(db.Model):
    __tablename__ = "orders"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"))
    order_date = Column(DateTime, default=datetime.utcnow)
    delivery_date = Column(DateTime, nullable=False)
    delivery_address = Column(Text)
    special_instructions = Column(Text)
    total_price = Column(Numeric(10, 2))
    status = Column(String(50), default="en attente")
    payment_method = Column(String(50))
    is_paid = Column(Boolean, default=False)

    order_items = relationship("OrderItem", backref="order", lazy=True)

    def __init__(self, **kwargs):
        super(Order, self).__init__(**kwargs)

# --- DÉTAILS DES COMMANDES ---
class OrderItem(db.Model):
    __tablename__ = "order_items"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    order_id = Column(String(36), ForeignKey("orders.id"))
    dish_id = Column(String(36), ForeignKey("dishes.id"))
    quantity = Column(Integer, nullable=False, default=1)
    unit_price = Column(Numeric(10, 2))

    def __init__(self, **kwargs):
        super(OrderItem, self).__init__(**kwargs)





























# from app.extensions import db
# from flask_login import UserMixin
# from datetime import datetime

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     # Relation : permet de faire role.users pour voir tous les membres
#     users = db.relationship('User', backref='role', lazy=True)




# class User(db.Model, UserMixin):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)
#     phone = db.Column(db.String(20))
#     address = db.Column(db.Text)
#     preferred_payment_method = db.Column(db.String(50))
    
#     # Clé étrangère vers Role
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
#     # Date de création automatique
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
#     # Relation : un utilisateur peut avoir plusieurs commandes
#     orders = db.relationship('Order', backref='customer', lazy=True)
    
#     def __repr__(self):
#         return f"<User {self.username}>" # Ca permet d'afficher le nom de l'utilisateur au lieu de <User 1> ou <User 2> dans la console lors du débogage, ce qui est plus lisible et pratique pour identifier les utilisateurs.
#         # https://docs.sqlalchemy.org/en/21/orm/quickstart.html
#         # https://stackoverflow.com/questions/55713664/sqlalchemy-best-way-to-define-repr-for-large-tables



# class Dish(db.Model):
#     __tablename__ = 'dishes'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     category = db.Column(db.String(50)) # Ex: Entrée, Plat, Dessert, Boisson
#     description = db.Column(db.Text)
#     price = db.Column(db.Numeric(10, 2), nullable=False)
#     image_url = db.Column(db.String(255))
#     is_active = db.Column(db.Boolean, default=True)
#     max_daily_quantity = db.Column(db.Integer, default=20)
    
#     # Relation : un plat peut être dans plusieurs commandes
#     order_items = db.relationship('OrderItem', backref='dish', lazy=True)
    
#     def __repr__(self):
#         return f"<Dish {self.name}>" # Représentation du plat pour le débogage et l'affichage dans la console




# class Order(db.Model):
#     __tablename__ = 'orders'
#     id = db.Column(db.Integer, primary_key=True)
    
#     # Clé étrangère vers User
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
#     order_date = db.Column(db.DateTime, default=datetime.utcnow)
#     delivery_date = db.Column(db.DateTime, nullable=False)
#     delivery_address = db.Column(db.Text)
#     special_instructions = db.Column(db.Text) # Ex: Pas d'oignons, code porte...
#     total_price = db.Column(db.Numeric(10, 2))
#     status = db.Column(db.String(50), default='en attente')
#     payment_method = db.Column(db.String(50)) # Ex: Cash, Twint, Carte
#     is_paid = db.Column(db.Boolean, default=False)
    
#     # Relation : une commande peut avoir plusieurs plats (order_items)
#     order_items = db.relationship('OrderItem', backref='order', lazy=True)
    
#     def __repr__(self):
#         return f"<Order {self.id} - User {self.user_id} - Status {self.status}>"




# class OrderItem(db.Model):
#     __tablename__ = 'order_items'
#     id = db.Column(db.Integer, primary_key=True)
    
#     # Clé étrangère vers Order
#     order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    
#     # Clé étrangère vers Dish
#     dish_id = db.Column(db.Integer, db.ForeignKey('dishes.id'))
    
#     quantity = db.Column(db.Integer, nullable=False)
#     unit_price = db.Column(db.Numeric(10, 2))

