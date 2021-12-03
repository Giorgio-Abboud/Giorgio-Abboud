# Programme qui calcule la moyenne

# Création de la fonction
def compteMoyenne(num):
    # Transforme les nombres en liste
    liste = list(eval(num))

    # Calcule la moyenne
    moyenne = sum(liste)/len(liste)

    return moyenne

# Demande pour les nombres
num = input("Inscrivez des nombres séparer par des virgules pour trouvers leur moyenne : ")

# Affiche le résultat
moyenne = compteMoyenne(num)
print("La moyenne est", moyenne)
