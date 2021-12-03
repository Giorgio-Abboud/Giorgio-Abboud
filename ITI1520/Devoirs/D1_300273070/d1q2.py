# Programme qui converti les livres et onces en kilogrammes avec une fonction

# Création de la fonction
def convertEnKilos(livres, onces):
    # Calcule le nombre de kilogrammes
    livreEnKilo = float(livres) / 2.20462262
    onceEnKilo = float(onces) / 35.273962
    kilogrammes = float(livreEnKilo) + float(onceEnKilo)
    return float(kilogrammes)

# Demande pour les livres et onces
livres = float(input("Inscrivez le nombre de livres : "))
onces = float(input("Inscrivez le nombre d'onces : "))

# Affiche la réponse
kilogrammes = convertEnKilos(livres, onces)
print("{0} livres et {1} onces égalent à {2} kilogrammes"
      .format(livres, onces, kilogrammes))
