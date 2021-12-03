# Programme qui insère des espaces entre le nom inséré par l'utilisateur

# Création de la fonction espaces
def espaces(nom):
    # Insère des espaces
    nom = nom.replace("", " ")
    nom = nom.strip()
    # Renvoie la réponse
    return nom

# Demande pour un mot
nom = str(input("Inscrivez un mot : "))

# Affiche la réponses
print(espaces(nom))
