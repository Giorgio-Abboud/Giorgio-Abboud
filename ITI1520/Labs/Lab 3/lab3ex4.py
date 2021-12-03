# Programme qui trouve le nombre de racines réelles selon l'équation quadratique
# Importation de module
import math

# Demande pour les valeures de a, b et c
a = int(input("Inscrivez la valeure de a : "))
b = int(input("Inscrivez la valeure de b : "))
c = int(input("Inscrivez la valeure de c : "))

# Calcule le nombre et affiche la réponse
if ((b**2)-(4*a*c))>0:
    racine2 = "Il y a 2 racines réelles"
    print("{0}".format(racine2))

elif ((b**2)-(4*a*c))==0:
    racine1 = "Il y a 1 racine réelle"
    print("{0}".format(racine1))

else:
    racine0 = "Il n'y a aucune racine réelle"
    print("{0}".format(racine0))
