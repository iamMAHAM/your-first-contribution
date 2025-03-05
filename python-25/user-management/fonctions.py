import json
import fonctions

def list_users():
    """Affiche la liste des utilisateurs enregistrés."""
    bd_content = fonctions.load_db()  # On charge les données du fichier JSON
    users = bd_content.get("users", [])  # On récupère la liste des utilisateurs

    if not users:  # Si la liste est vide
        print("Aucun utilisateur enregistré.")
        return

    print("Liste des utilisateurs :")
    for user in users:  # On parcourt chaque utilisateur
        print(f"Email: {user['email']}, Rôle: {user['role']}")  # On affiche son email et son rôle
