# Programme qui trie une liste et trouve le nombre de pas de façon efficace

# Création d'une fonction
def tri_par_insertion(L):
    # Donne une valeur a NPas
    NPas = 0

    # compte le nombres de pas et tri la liste
    for i in range(0, len(L)):
        j = i
        num = L[j]
        NPas += 1
        while j > 0 and num < L[j-1]:
            L[j] = L[j-1]
            j = j - 1
            NPas += 1
        L[j] = num

    # Retourne le résultat
    return NPas
    
# Demande pour une liste et un nombre a chercher
L = input("Insérez des nombres séparer par des virgules : ")
L = list(eval(L))

# Affiche la réponse
print("Nombres de pas : ", tri_par_insertion(L))
print(L)
