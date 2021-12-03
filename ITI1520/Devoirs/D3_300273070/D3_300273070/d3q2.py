# Programme qui affiche dix questions aléatoires d'addition et de multiplication

# Importation de module
import random
    
# Création des questions aléatoires
def effectuezTest():
    resultat = False
    questions = 0
    bonne_reponse = 0

    # Questions d'additions ou de multiplication au hasard
    while questions < 10:
        for add_ou_multi in range(10):
            add_ou_multi = random.randint(0, 1)
    
        # Questions d'addition
        if add_ou_multi == 0:
            # Création des nombres au hasard et de la question
            n1 = random.randint(0, 9)
            n2 = random.randint(0, 9)
            reponse_eleve = int(input("{0} + {1} = ".format(n1, n2)))
            # Calcule la réponse et affiche le résultat
            reponse = (n1 + n2)
            # Compteur de questions posées
            questions = questions + 1
            # Calcule le résultat final
            if reponse_eleve == reponse:
                resultat = True
            else:
                resultat = False
            # Détermine le résultat final
            if resultat == True:
                bonne_reponse = bonne_reponse + 1
            else:
                print("Incorrecte, la bonne réponse est {0}".format(reponse))
                
        # Question multiplication
        else:
            # Création des nombres au hasard
            n1 = random.randint(0, 9)
            n2 = random.randint(0, 9)
            reponse_eleve = int(input("{0} * {1} = ".format(n1, n2)))
            # Calcule la réponse et affiche le résultat
            reponse = (n1 * n2)
            # Compteur de questions posées
            questions = questions + 1
            # Calcule le résultat final
            if reponse_eleve == reponse:
                resultat = True
            else:
                resultat = False
            # Détermine le résultat final
            if resultat == True:
                bonne_reponse = bonne_reponse + 1
            else:
                print("Incorrecte, la bonne réponse est {0}".format(reponse))

    return bonne_reponse

# Message du programme
print("Ce programme affichera un test de 10 questions aléatoires")

# Apelle la fonction
bonne_reponse = effectuezTest()

# Afficher la réponse finale
print(("{0} réponse(s) correcte(s)").format(bonne_reponse))

# Calculer les points accumulé par l'élève pour afficher le texte approprié
if bonne_reponse > 6:
    print("Félicitations!")
else:
    print("Demandez à votre enseignant(e) de vous aider")

