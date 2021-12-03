# Programme qui trouve si un nombre est divisible par 2 et 3

# Demande pour le nombre
n = int(input("Inscrivez le nombre : "))

# Calcule le nombre et affiche la réponse
if (n%2==0) and (n%3==0):
    resultat2 = "Divisible par 2 et par 3"
    print("{0}".format(resultat2))

elif (n%2==0) or (n%3==0):
    resultat1 = "Divisible par 2 ou par 3"
    print("{0}".format(resultat1))

else:
    resultat0 = "Pas divisible ni par 2 et ni par 3"
    print("{0}".format(resultat0))
