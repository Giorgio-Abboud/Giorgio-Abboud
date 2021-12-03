# Programme qui dépace tous les zéros à la fin de la liste

# Création de la fonction
def move_zero_v2(x):
    # Organise la liste et créer le résultat
    x.sort(key=lambda i: i == 0)

# Créer le tuple
x = input("Inscrivez une liste de nombres séparer par des virgules : ")
x = list(eval(x))

# Affiche la réponse
z = move_zero_v2(x)
print(x, z)
