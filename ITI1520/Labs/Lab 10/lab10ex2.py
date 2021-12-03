# Programme avec une classe CompteBancaire qui permet des transactions

# La classe CompteBancaire
class CompteBancaire(object):

    # La fonction __init__
    def __init__(self, nom, somme):
        self.nom = nom
        self.somme = somme

    # La fonction qui initialise les dépots
    def depot(self, somme):
        self.somme = somme

    # La fonction qui initialise les retraites
    def retrair(self, somme):
        self.somme = somme

    # La fonction qui affiche le résultat
    def affiche(self):
        print("Le solde du compte bancaire de " + str(nom) + " est de " + str(somme) + "$")

# La classe CompteEpargne
class CompteEpargne(object):

    # La fonction __init__
    def __init__(self, valeur, nombreMois):
        self.valeur = valeur
        self.nombreMois = nombreMois

    # La fonction qui initialise le taux
    def changeTaux(self, valeur):
        self.valeur = valeur

    # La fonction qui initialise la capitalisation
    def capitalisation(self, nombreMois):
        self.nombreMois = nombreMois
        print("Capitalisation sur " + str(nombreMois) + " mois au taux mensuel de " + str(self.valeur) + " %")

    # La fonction qui affiche le résultat
    def affiche_cap(self, somme_cap):
        print("Le solde du compte bancaire de " + str(nom) + " est de " + str(somme_cap) + "$")

# CompteBancaire initiale
stock = CompteBancaire("Dupont", 1000)

# La fonction __init__
nom = str(input("Qui est le propriétaire de l'argent? : "))
if nom == "":
    nom = "Dupont"
somme = input("Qu'elle est votre somme initiale? : ")
if somme == "":
    somme = 1000
stock.__init__(nom, somme)

# Change le montant d'argent par dépot
depot = input("Inscris le montant d'argent à déposer : ")
somme = int(somme) + int(depot)
stock.depot(somme)

# Change le montant d'argent par retraites
retraites = input("Inscris le montant d'argent à retraire : ")
somme = int(somme) - int(retraites)
stock.retrair(somme)

# Affiche le résultat
stock.affiche()

# CompteEpargne initiale
stock = CompteEpargne(nom, somme)

# Change le taux
valeur = float(input("Inscris la valeur du taux : "))
if valeur == "":
    valeur = 0.3
stock.changeTaux(valeur)

# Change le nombre de mois
nombreMois = int(input("Inscris le nombre de mois : "))
if nombreMois == "":
    nombreMois = 0
stock.capitalisation(nombreMois)

# Affiche le résultat
somme_cap = (somme * (1+(valeur/100))**nombreMois)
stock.affiche_cap(somme_cap)
