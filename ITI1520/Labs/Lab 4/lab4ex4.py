# Programme qui calcule le factoriel d'un nombre insrit

# Importation de module
import math

# Créer du programme principale
def calculeFact(n):
    factorielle = math.factorial(n)
    return factorielle

# Demande pour le nombre deviné du joueur
n = int(input("Inscrivez un chiffre pour calculer sa factorielle : "))

# Si le chiffre n'est pas en entier
while n < 0:
    n = int(input("Inscrivez un chiffre non négatif : "))

# Affiche la réponse
factorielle = calculeFact(n)
print("La factorielle de {0} est {1}".format(n, factorielle))

