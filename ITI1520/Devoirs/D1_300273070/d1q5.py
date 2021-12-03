# Programme qui trouve la valeure de "y"
import math

# Création de la fonction
def fun(x):
    # Calcule la valeure de "y"
    y = (math.log10(x+3))/4
    return float(y)

# Demande pour la valeure de "x"
x = float(input("Inscrivez la valeure de la variable x : "))

# Affiche la réponse
y = fun(x)
print("La valeure de la variable y est de {0}".format(y))
