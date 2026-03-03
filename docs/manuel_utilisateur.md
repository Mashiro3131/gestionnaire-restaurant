# Mannuel d'installation

### Créer le fichier restaurant.db

```python
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
```

Ca devrait crée le fichier restaurant.db dans le dossier instance/ avec les tables User, Dish, Order et OrderItem

### Tester si la BD s'est bien créée

```powershell
ls -Recurse restaurant.db

# Résultat attendu :
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---l        03.03.2026     11:33              0 restaurant.db
```

*[Documentation](https://docs.sqlalchemy.org/en/20/core/engines.html)*

### Vérifier que les tables ont bien été créées
```PYTHON
# Voir les tables créées
app = create_app()
with app.app_context():
    # Cette commande liste les tables détectées par SQLAlchemy
    print(db.inspect(db.engine).get_table_names())

# Si rien apparait, on relance la création
with app.app_context():
    db.create_all()
    print("Tables créées :", db.inspect(db.engine).get_table_names())

# Résultat attendu :
>>> with app.app_context():
...     db.create_all()
...     print("Tables créées :", db.inspect(db.engine).get_table_names())
... 
Tables créées : ['dishes', 'order_items', 'orders', 'roles', 'users']