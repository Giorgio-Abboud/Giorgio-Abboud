# Programme qui créer un jeu de devinette en génèrant un numéro entre 1 et 10

# Importation de module
import random

# Nombres d'essaies
numEssaie = 1

# Créer du programme principale
def devine(reponse, numero, numEssaie):
        
    while reponse != numero:    
        # Si la réponse est plus haute
        if reponse > numero:
            print("Désolé! Votre réponse est plus haute du numéro à deviner.")
            # Si le chiffre n'est pas deviné
            numEssaie = numEssaie + 1
            reponse = int(input("Inscrivez un chiffre entre 1 et 10: "))

        # Si la réponse est plus basse
        else:
            print("Désolé! Votre réponse est plus basse du numéro à deviner.")
            # Si le chiffre n'est pas deviné
            numEssaie = numEssaie + 1
            reponse = int(input("Inscrivez un chiffre entre 1 et 10: "))

    # Si la réponse est correcte
    if reponse == numero:
        return numEssaie

# Demande pour le nombre deviné du joueur
reponse = int(input("Inscrivez un chiffre entre 1 et 10: "))

# Si le chiffre n'est pas en entier
while reponse < 1 or reponse > 10 :
    reponse = int(input("Inscrivez un chiffre entre 1 et 10: "))

# Création du numéro au hazard entre 1 et 10
numero = random.randint(1, 10)

# Affiche la réponse
numEssaie = devine(reponse, numero, numEssaie)
print("Bravo! Vous avez deviné le nombre au hazard après {0} essaie(s)".format(numEssaie))

