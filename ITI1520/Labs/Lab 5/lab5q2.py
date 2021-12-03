# Programme qui calcule la moyenne

# Création de la fonction
def compteNote(num):
    # Transforme les nombres en liste
    liste = list(eval(num))

    #Création d'une liste
    resultat = []

    # Calcule la moyenne
    moyenne = sum(liste)/len(liste)
    resultat.append(moyenne)

    # Trouve la valeur minimale et maximale
    numMin = min(liste)
    resultat.append(numMin)
    numMax = max(liste)
    resultat.append(numMax)

    return resultat

# Demande pour les nombres
num = input("Inscrivez vos notes séparer par des virgules pour trouvers leur moyenne, la note maximale et la not minimale : ")

# Affiche le résultat
resultat = compteNote(num)
print(resultat)
