# résoudre l'équation 10 puissance 4y = x+3

import math

def fun(x):
    y= math.log10(x+3)
    y=y/4
    return y

x =float(input("Entrez un nombre positif: "))   
print("La solution y a votre equation est : ", fun(x))


