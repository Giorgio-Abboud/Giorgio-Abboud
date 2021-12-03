# Programme qui détermine des valeurs associé aux années lumières

# Création de la fonction
# Calcule les secondes lumières
def seconde_lumiere_annee():
    secLumAnnee = 365.26*86400
    return (secLumAnnee)

def seconde_lumiere(annee_lumiere):
    secLumAnnee = seconde_lumiere_annee()
    secondeLumiere = annee_lumiere*secLumAnnee
    return (secondeLumiere)

# Calcule la distance lumiere parcouru
def distance_lumiere(annee_lumiere):
    secondeLumiere = seconde_lumiere(annee_lumiere)
    distanceFinal = secondeLumiere*300000
    return distanceFinal

# Calcule la distance lumiere parcouru des soleils
def distance_soleil(annee_lumiere_soleil1, annee_lumiere_soleil2):
    # Calcule les secondes lumières
    secLumAnnee = seconde_lumiere_annee()
    distanceSoleil = (annee_lumiere_soleil1 + annee_lumiere_soleil2)*secLumAnnee*300000
    return float(distanceSoleil)

# Demande pour le nombre d'années-lumières
annee_lumiere = float(input("Inscrivez le nombre d'années-lumières : "))

# Demande pour le nombre d'années-lumières des soleils
annee_lumiere_soleil1 = float(input("Inscrivez le nombre d'années-lumières du premier soleil : "))
annee_lumiere_soleil2 = float(input("Inscrivez le nombre d'années-lumières du deuxième soleil : "))

# Affiche les réponses
secondeLumiere = seconde_lumiere(annee_lumiere)
print("Le nombre de secondes-lumières est de {}".format(secondeLumiere))

distanceFinal = distance_lumiere(annee_lumiere)
print("La distance est de {} kilomètres".format(distanceFinal))

distanceSoleil = distance_soleil(annee_lumiere_soleil1, annee_lumiere_soleil2)
print("La distance entre les soleils est de {} kilomètres".format(distanceSoleil))
