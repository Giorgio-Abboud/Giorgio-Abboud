# Programme qui dépace tous les zéros à la fin de la liste

# Création de la fonction
def move_zero_v3(x):
    # Organise la liste et créer le résultat
    a = 0
    
    for i in range(0, len(x)):
        if x[i] != 0:
            x[a] = x[i]
            a = a + 1

    for i in range(a, len(x)):
        x[i] = 0

# Créer le tuple
x = input("Inscrivez une liste de nombres séparer par des virgules : ")
x = list(eval(x))

# Affiche la réponse
t = move_zero_v3(x)
print(x, t)
