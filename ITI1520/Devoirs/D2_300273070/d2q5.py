# Programme qui affiche un résultat selon la couleur du feu de circulation inscrit

# Demande pour la couleure du feu de circulation
feu_couleur = str(input("Inscrivez la couleur du feu de circulation (ex : rouge, jaune, vert): "))

# Calcule affiche le texte approprié selon la couleur inscrite
if feu_couleur == "rouge":
    print("Arrêtez!")

elif feu_couleur == "jaune":
    print("Ralentissez!")

elif feu_couleur == "vert":
    print("Avancez!")

else:
    print("Faites attention!")
