"""
Fichier pour les modèles de données de l'application. 
Définit les classes représentant les tables de la base de données (User, Dish, Order, OrderItem, Role)
"""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, Numeric, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from app.extensions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


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
    city = Column(String(100))
    zip_code = Column(String(10))
    preferred_payment_method = Column(String(50))
    role_id = Column(String(36), ForeignKey("roles.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship("Order", backref="customer", lazy=True)

    # Hache le mdp pour plus de sécurité
    def set_password(self, password_brut):
        self.password = generate_password_hash(password_brut)
    
    # Vérifie le mot de passe par rapport au hash stocké dans "password"
    def check_password(self, password_brut):
        
        return check_password_hash(str(self.password), password_brut)

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

