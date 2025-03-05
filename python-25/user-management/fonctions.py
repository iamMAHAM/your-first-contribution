import json, random
file_name = "db.json"

def forgot_password(email: str):
    flag_mail = False
    with open(file_name, "r") as f:
        db_content = json.load(f)
        users = db_content["Users"]

    for user in users:  # Parcours de la liste des comptes enregistrés

        if email == user["email"]:  # Vérification de l'existence de l'email
            verification_code = str(random.randint(1000, 9999))  # Génération d'un code aléatoire à 4 chiffres
            print(f"Code de vérification : {verification_code}")
            user_code = input("Veuillez entrer le code affiché : ")

            while user_code != verification_code:
                print("Le code saisi est incorrect. ")
                verification_code = str(random.randint(1000, 9999)) # Génération d'un code aléatoire à 4 chiffres
                print(f"Code de vérification : {verification_code}")
                user_code = input("Veuillez entrer le code affiché : ")

            new_password = input("Entrez votre nouveau mot de passe : ")
            user["password"] = new_password  # Mise à jour du nouveau mot de passe

            with open(file_name, "w") as f:  # Réécriture du fichier avec le nouveau mot de passe
                json.dump(db_content, f)
            print("Mot de passe mis à jour avec succès !")