# Programme qui trie une liste et trouve le nombre de pas de façon efficace

# Création d'une fonction
def recherche_binaire(liste, v):

    # Associe des valeurs au variables
    NPas = 0
    trouve = False

    # Trouve le nombres de pas
    position = -1
    # i et j delimitent la section de recherche
    i = 0
    j = len(liste) - 1 
    while i != j + 1:
        m = (i + j) // 2 # trouve le milieu
        if liste[m] == v: # si on a trouve retourne la position
            position = m
            NPas += 1
            trouve = True
            break
        elif liste[m] < v: # cherche a droite 
            i = m + 1
            NPas += 1
        else: # cherche a gauche
            j = m - 1
            NPas += 1

    # Retourne les résultats
    print("Nombre de pas", NPas)        
    return trouve
    
# Demande pour une liste et un nombre a chercher
liste = input("Insérez des nombres séparer par des virgules : ")
liste = list(eval(liste))
liste.sort()
v = int(input("Insérez le nombre rechercé : "))

# Affiche la réponse
print(recherche_binaire(liste, v))
