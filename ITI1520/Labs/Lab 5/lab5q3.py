# Programme qui calcule la portée de la balle

# Importation de module
import math

# Création de la fonction
def distanceBalle(v, x):
    # La liste des degrées
    degree = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

    # Si l'angle est de 0 degrée
    if x == 9:
        distance = 0
        return distance
    
    # Calcule la distance de la balle
    distance = ((2*(v**2))*(math.sin(math.radians(degree[x])))*(math.cos(math.radians(degree[x]))))/9.8
    
    # Renvoie la distance de la balle
    return distance

# Demande pour la vitesse et l'angle
v = float(input("Inscrivez la vitesse de la balle en m/s : "))
while v < 0:
    v = float(input("La vitesse de la balle en m/s doit être positive : "))
    
x = int(input("Inscrivez un chiffre entre 0 et 9 qui définit l'angle de la balle (ex : 3 égale à 30 degrées) : "))
while x < 0 or x > 9:
    x = int(input("Inscrivez un chiffre entre 0 et 9 : "))

# Affiche le résultat
distance = distanceBalle(v, x)
print("La distance de la balle est de {0} mètres".format(distance))
