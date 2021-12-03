# Programme qui calcule l'écart-type
# Importation de module
import statistics

# Création de la fonction
def type_ecart(num):
    # Transforme les nombres en liste
    liste = list(eval(num))

    #Création d'une liste
    resultat = []

    # Calcule l'écart-type
    ecart = statistics.stdev(liste)
    resultat.append(ecart)

    return resultat

# Demande pour les nombres
num = input("Inscrivez vos nombres séparer par des virgules pour trouvers leur écart-type : ")

# Affiche le résultat
resultat = type_ecart(num)
print(resultat)
