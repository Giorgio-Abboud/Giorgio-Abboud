# Programme qui détermine si un entier est un carré parfait
#importation de module
import math

# Demande pour la valeure de l'entier
entier = int(input("Inscrivez la valeure de votre entier : "))

# Arrondit le nombre
racine = math.sqrt(entier)
carree = round(racine, 0)

# Calcule le carré et affiche la réponse
if entier == (carree**2):
    print("{0} est un carré parfait et sa racin carrée est {1}".format(entier, carree))

else:
    print("{0} n'est pas un carré parfait".format(entier))
