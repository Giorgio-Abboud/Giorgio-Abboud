# Programme qui trie une liste en order ascendant et trouve le nombre de pas

# Création d'une fonction
def trier(liste):

    # Donne une valeur à NPas
    NPas = 0
    
    # Trie la liste
    liste = list(eval(liste))
    liste.sort()

    # Compter le nombre de pas
    NPas += 1
    
    # Retourne les résultats
    return NPas       
    
# Demande pour une liste et un nombre a chercher
liste = input("Insérez des nombres séparer par des virgules : ")

# Affiche la réponse
print("Nombre de pas", trier(liste))
print(liste)
