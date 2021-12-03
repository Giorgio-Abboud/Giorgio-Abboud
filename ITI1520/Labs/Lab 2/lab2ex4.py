# Programme calcule la note finale
# Importation des modules
import math

# Calcule la note finale
def surfaceTriangle(cote1, cote2, cote3):
    p = cote1+cote2+cote3
    surface_triangle = math.sqrt(p*(p-2*cote1)*(p-2*cote2)*(p-2*cote3))/4
    return surface_triangle

# Demande pour les côtés
cote1 = float(input("Inscrivez la mesure du premier côté : "))
cote2 = float(input("Inscrivez la mesure du deuxième côté : "))
cote3 = float(input("Inscrivez la mesure du troisième côté : "))

# Affiche les résultats
surface_triangle = surfaceTriangle(cote1, cote2, cote3)
print("La surface du triangle est de {0} unités carrés".format(surface_triangle))
