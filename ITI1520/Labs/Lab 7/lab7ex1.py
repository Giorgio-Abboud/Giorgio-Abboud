# Programme qui prend un tuple et retourne un dictionnaire

# Création de la fonction
def hosto_n(x):
    # Création d'une liste et d'un dictionnaire
    liste = []
    dictionnaire = {}

    # Met les nombres dans la liste et un dictionnaire
    for n in x:
        liste.append(n)
    liste.sort()
    for num in liste:
        dictionnaire[num] = dictionnaire.get(num, 0) + 1

    # Retroune le résultat
    return dictionnaire

# Créer le tuple
t = input("Inscrivez une liste de nombres séparer par des virgules : ")
t = tuple(int(x) for x in t.split(","))

# Affiche la réponse
dictionnaire = hosto_n(t)

liste_item = list(dictionnaire.items())
print(liste_item)
