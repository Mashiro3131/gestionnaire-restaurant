# Mannuel d'installation

### Créer la base de données et le fichier restaurant.db

#### 1. Ouvrir le terminal


#### 2. Lancer une session Python interactive

```powershell
python


```python
# 1. Ouvrir le terminal
# 2. Lancer une session Python interactive
# 
with app.app_context():
    try:
        db.drop_all()
        db.create_all()
    except Exception as e:
        print("Erreur lors de la création des tables :", e)
    else:
        print("Tables créées :", db.inspect(db.engine).get_table_names())
```

Ca devrait crée le fichier restaurant.db dans le dossier instance/ avec les tables User, Dish, Order et OrderItem
Il faut faire at

### Tester si la BD s'est bien créée

```powershell
ls -Recurse restaurant.db

# Résultat attendu :
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---l        03.03.2026     11:33              0 restaurant.db
```

*[Documentation](https://docs.sqlalchemy.org/en/20/core/engines.html)*

### Résultat attendu :
```cmd
>>> app = create_app()
>>> with app.app_context():
...     try:
                db.drop_all()
...             db.create_all()
...     except Exception as e:
...             print("Erreur lors de la création des tables :", e)
...     else:
...             print("Tables créées :", db.inspect(db.engine).get_table_names())
... 
Tables créées : ['dishes', 'order_items', 'orders', 'roles', 'users']
```
