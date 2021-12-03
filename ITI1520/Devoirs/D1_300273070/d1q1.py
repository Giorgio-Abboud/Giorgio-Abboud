# Programme qui converti les livres et onces en kilogrammes

# Demande pour les livres et onces
livres = float(input("Inscrivez le nombre de livres : "))
onces = float(input("Inscrivez le nombre d'onces : "))

# Calcule le nombre de kilogrammes
kilogrammes = (float(livres) / 2.20462262) + (float(onces) / 35.273962)

# Affiche la réponse
print("{0} livres et {1} onces égalent à {2} kilogrammes"
      .format(livres, onces, kilogrammes))
