# Programme qui retourne True si la somme de 3 éléments consécutives est 0

# Création de la fonction
def somme_de_trois(x):
    # Création d'une liste
    liste = []

    # Met les nombres dans la liste
    for num in x:
        liste.append(int(num))

    # Calcule la somme des 3 éléments consécutives
    for i in range(0, len(liste) - 2):
        if liste[i] + liste[i+1] + liste[i+2] == 0:
            booly = True
            break
        else :
            booly = False

    # Retourne le résultat
    return booly

# Créer le tuple
t = input("Inscrivez une liste de nombres séparer par des virgules : ")
t = tuple(int(x) for x in t.split(","))
print(somme_de_trois(t))
