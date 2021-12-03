# Programme qui recommende une activité selon la température

# Demande pour la température
temperature = int(input("Inscrivez la température : "))

# Calcule le nombre et affiche la réponse
if temperature >= 80:
    activite1 = "Natation"
    print("{0}".format(activite1))

elif temperature < 80 and temperature >=60:
    activite2 = "Soccer"
    print("{0}".format(activite2))

elif temperature < 60 and temperature >=40:
    activite3 = "Volleyball"
    print("{0}".format(activite3))

else:
    activite4 = "Ski"
    print("{0}".format(activite4))
