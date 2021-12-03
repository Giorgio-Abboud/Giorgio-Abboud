# Programme qui prend une matrice et incrément 1 deux fois

# Création d'une fonction
def ajoute(matrice):
    # Copie la première matrice et ajoute 1 a toutes les valeurs
    ajoute = []
    for i in range(len(matrice)):
        ajoute.append([])
        for j in range(len(matrice[0])):
            ajoute[i].append((matrice[i][j])+1)

    # Retourne la matrice
    return ajoute

def ajoute_V2(ajoute):
    # Copie la première matrice et enlève 1 a toutes les valeurs
    ajoute_V2 = []
    for i in range(len(ajoute)):
        ajoute_V2.append([])
        for j in range(len(ajoute[0])):
            ajoute_V2[i].append((ajoute[i][j])+1)

    # Retourne la matrice
    return ajoute_V2

# Création de la matrice A
print("Entrez les nombres avec des espaces entre les colonnes.")
print("Une rangee par ligne, et une ligne vide a la fin.")
matrice = []
while True:
    ligne = input()
    if not ligne: break
    valeurs = ligne.split()
    rangee = [int(val) for val in valeurs]
    matrice.append(rangee)

# Affiche la réponse
print("La matrice est : ")
print(matrice)

print("Après exécution de la fonction ajoute, la matrice est : ")
print(ajoute(matrice))

ajoute = ajoute(matrice)

print("Une nouvelle matrice créée avec ajoute_V2 : ")
print(ajoute_V2(ajoute))

print("Après exécution de la fonction ajoute_V2, la matrice initiale est : ")
print(ajoute)
