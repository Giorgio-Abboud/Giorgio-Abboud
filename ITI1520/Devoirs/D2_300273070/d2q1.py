# Programme qui calcule l'indice de masse corporelle

# Demande pour le poid et l'hauteur de l'utilisateur
poid = float(input("Inscrivez votre poid en kilogrammes : "))
hauteur = float(input("Inscrivez votre hauteure en mètres : "))

# Calcule l'IMC et affiche la réponse
if poid/(hauteur**2)<18.5:
    maigre = poid/(hauteur**2)
    print("Votre IMC est {0}".format(maigre))
    print("Maigreur")

elif poid/(hauteur**2)>=18.5 and poid/(hauteur**2)<25:
    ideal = poid/(hauteur**2)
    print("Votre IMC est {0}".format(ideal))
    print("Poids idéal")

elif poid/(hauteur**2)>=25 and poid/(hauteur**2)<30:
    surpoid = poid/(hauteur**2)
    print("Votre IMC est {0}".format(surpoid))
    print("Surpoids")

else:
    obesite = poid/(hauteur**2)
    print("Votre IMC est {0}".format(obesite))
    print("Obésité")
