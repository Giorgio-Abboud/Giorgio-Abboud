# Programme qui calcule et affiche le résultat de la division entière et le restant

# Demande pour les valeurs
valeur1 = int(input("Inscrivez la première valeure : "))
valeur2 = int(input("Inscrivez la deuxième valeure : "))

# Calcule la division entière et le restant
totalEntier = valeur1//valeur2
totalRestant = valeur1%valeur2

# Affiche les résultats
print("{0} // {1} = {2}".format(valeur1, valeur2, totalEntier))
print("{0} % {1} = {2}".format(valeur1, valeur2, totalRestant))
