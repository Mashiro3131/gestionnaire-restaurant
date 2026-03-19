from werkzeug.security import generate_password_hash
from app import create_app, db
from app.models import User, Role, Dish
from colorama import Fore, Style


def seed_database():
    
    app = create_app()
    with app.app_context():
        try :
            print(Fore.LIGHTYELLOW_EX + "\n--- Nettoyage de la base de données ---")
            db.drop_all()
            db.create_all()


            # Création des Rôles
            print(Fore.LIGHTGREEN_EX + "\n--- Création des rôles ---")
            admin_role = Role(name="admin")
            staff_role = Role(name="staff")
            client_role = Role(name="client")
            db.session.add_all([admin_role, client_role, staff_role])
            db.session.commit() # On commit pour avoir les IDs des rôles



            # 2. Création des Utilisateurs
            print(Fore.LIGHTGREEN_EX + "--- Création des utilisateurs ---")
            # Un compte Admin pour toi
            admin_user = User(
                first_name="Iko",
                last_name="Admin",
                username="admin_iko",
                email="admin@ikos.ch",
                password=generate_password_hash("Admin123!"), # Toujours hasher !
                role=admin_role
            )
            
            # Un compte Staff pour gérer les commandes et le menu
            staff_user = User(
                first_name="Iko",
                last_name="Staff",
                username="sophie_staff",
                email="staff@ikos.ch",
                password=generate_password_hash("Staff123!"),
                role=staff_role
            )

            # Un compte Client pour tester
            client_user = User(
                first_name="Nico",
                last_name="Mengsien",
                username="nico_mengsien",
                email="nico.mengisen@gmail.com",
                password=generate_password_hash("Client123!"),
                role=client_role
            )
            db.session.add_all([admin_user, staff_user, client_user])



            # Création du Menu
            print(Fore.LIGHTGREEN_EX + "--- Création du menu ---")
            dishes = [
                Dish(
                    name="Le Manchot Gourmet",
                    category="Burger",
                    description="Burger Angus juteux, fromage d’alpage affiné fondant (Gruyère AOP), oignons confits au vin rouge, mayonnaise fumée maison, pickles artisanaux et roquette, dans un pain brioché toasté au beurre fermier.",
                    price=26.50,
                    image_url=None
                    #image_url="burger_gourmet.jpg"
                ),
                Dish(
                    name="L'Antarctique",
                    category="Poisson",
                    description="Pavé de saumon frais rôti, accompagné de légumes de saison et d’une délicate sauce citronnée.",
                    price=24.00,
                    image_url=None
                    #image_url="saumon_plate.jpg"
                ),
                Dish(
                    name="Ragu du Nord",
                    category="Pâtes",
                    description="Tagliatelles fraîches maison, ragù de cerf mijoté 6 heures, champignons sautés, parmesan affiné, touche d’agrumes et herbes fraîches.",
                    price=22.50,
                    image_url=None
                    #image_url="pasta_ragu.jpg"
                ),
                Dish(
                    name="Iko-Fries",
                    category="Accompagnement",
                    description="Frites de patate douce maison double cuisson, saupoudrées de sel de mer et accompagnées d’une sauce maison",
                    price=6.50,
                    image_url=None
                    #image_url="fries.jpg"
                ),
                Dish(
                    name="Aioli des Bois",
                    category="Sauces",
                    description="Aioli maison à base d'ail, airelles et romarin.",
                    price=2.00,
                    image_url=None
                    # image_url="fries.jpg"
                )       
            ]
        
            db.session.add_all(dishes)
            
        # Si y'a une erreur, on affiche l'erreur et on annule les changements
        except Exception as e:
            print(Fore.RED + "Erreur lors de l'ajout des plats :", e)
            db.session.rollback()
        
        # Si y'a pas eu d'erreur, feu vert pour query la db
        else:
            print(Fore.LIGHTGREEN_EX + "--- Plats ajoutés avec succès ! ---")
            # Query la db 
            db.session.commit()
        
        
        # Print des infos de connexion
        print(Fore.MAGENTA + "\n--- Base de données initialisée avec succès ! ---")
        print(Fore.LIGHTBLUE_EX + "\nAdmin : admin@ikos.ch / Admin123!")
        print(Fore.LIGHTBLUE_EX + "Staff : staff@ikos.ch / Staff123!")
        print(Fore.LIGHTBLUE_EX + "Client : nico.mengisen@gmail.com / Client123!")



if __name__ == "__main__":
    seed_database()