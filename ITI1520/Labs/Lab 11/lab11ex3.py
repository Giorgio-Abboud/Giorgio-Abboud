# Programme de l'algorithme d'Euclide

# Création d'une fonction
def pgcd(a, b):
    if a < b: 
        (a, b) = (b, a)
    if(a % b) == 0:
        return b 
    else:
        return (pgcd(b, a % b))

# Demande pour deux nombres
a = int(input("Entrez un nombre : "))
b = int(input("Entrez un autre nombre : "))

# Appèle la fonction
print(pgcd(a, b))
