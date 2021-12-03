# Programme avec une classe voiture qui permet d’instancier des objets reproduisant le comportement de voitures automobiles

# La classe voiture
class Voiture(object):

    # La fonction __init__
    def __init__(self, marque, couleur, pilote, vitesse):
        self.marque = marque
        self.couleur = couleur
        self.pilote = pilote
        self.vitesse = vitesse

    # La fonction __repr__
    def __repr__(self):
        return (repr(self.marque) + repr(self.couleur) + "pilotée par" + repr(self.pilote) + ", vitesse = " + repr(self.vitesse) + "m/s")

    # La fonction __eq__
    def __eq__(self, other):
        return (self.marque == other.marque and self.couleur == other.couleur and self.pilote == other.pilote and self.vitesse == other.vitesse)

    # La fonction qui modifies la marque et la couleur
    def voiture(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur

    # La fonction qui modifies le pilote
    def choix_conducteur(self, pilote):
        # Pilote
        self.pilote = pilote

    # La fonction qui modifies le taux et la duree
    def accelerer(self, taux, duree):
        self.taux = taux
        self.duree = duree
        vitesse = taux * duree
        self.vitesse = vitesse

    # La fonction qui affiche le résultat
    def affiche_tout(self):
        print(str(marque) + " " + str(couleur) + " pilotée par " + str(pilote) + ", vitesse = " + str(self.vitesse) + " m/s")

# Voiture initiale
stock = Voiture("Ford", "rouge", "personne", 0)

# Change la marque et la couleure de la voiture
marque = str(input("Inscris une marque de voiture : "))
if marque == "":
    marque = "Ford"
couleur = str(input("Inscris une couleure pour la voiture : "))
if couleur == "":
    couleur = "rouge"
stock.voiture(marque, couleur)

# Change le ou la pilote
pilote = str(input("Inscris le ou la pilote de la voiture : "))
if pilote == "":
    pilote = "personne"
stock.choix_conducteur(pilote)

# Change le taux et la duree
taux = float(input("Inscris un taux : "))
duree = float(input("Inscris une duree : "))
if pilote == "personne":
    taux, duree = 0, 0
stock.accelerer(taux, duree)

# Affiche le résultat
stock.affiche_tout()
