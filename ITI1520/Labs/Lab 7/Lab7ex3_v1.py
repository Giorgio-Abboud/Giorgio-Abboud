# Programme qui dépace tous les zéros à la fin de la liste

# Création de la fonction
def move_zero_v1(x):
    # Création de la liste
    tmp = []
    for i in x:
        tmp.append(int(i))

    # Organise la liste et créer le résultat
    tmp.sort(key=lambda i: i == 0)

    # Retourne le résultat
    return tmp

# Créer le tuple
x = input("Inscrivez une liste de nombres séparer par des virgules : ")
x = list(eval(x))

# Affiche la réponse
y = move_zero_v1(x)
print(x, y)
