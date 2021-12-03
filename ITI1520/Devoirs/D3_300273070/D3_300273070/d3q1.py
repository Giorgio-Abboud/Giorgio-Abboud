# Programme qui affiche dix questions aléatoires d'addition ou de multiplication

# Importation de module
import random
    
# Création des questions aléatoires
def effectuezTest(operation):
    bonne_reponse = 0
    
    # Questions d'addition
    if operation == 0:
        for i in range(10):
            # Création des nombres au hasard et de la question
            n1 = random.randint(0, 9)
            n2 = random.randint(0, 9)
            reponse_eleve = int(input("{0} + {1} = ".format(n1, n2)))
            # Calcule la réponse et affiche le résultat
            reponse = (n1 + n2)
            # Détermine le résultat final
            if reponse_eleve == reponse:
                bonne_reponse = bonne_reponse + 1
            else:
                print("Incorrecte, la bonne réponse est {0}".format(reponse))
            
            
    # Question multiplication
    else:
        for i in range(10):
            # Création des nombres au hasard
            n1 = random.randint(0, 9)
            n2 = random.randint(0, 9)
            reponse_eleve = int(input("{0} * {1} = ".format(n1, n2)))
            # Calcule la réponse et affiche le résultat
            reponse = (n1 * n2)
            # Détermine le résultat final
            if reponse_eleve == reponse:
                bonne_reponse = bonne_reponse + 1
            else:
                print("Incorrecte, la bonne réponse est {0}".format(reponse))

    # Calculer les points accumulé par l'élève pour afficher le texte approprié
    if bonne_reponse > 6:
        resultatFinal = ("Félicitations!")
        return resultatFinal, bonne_reponse
    else:
        resultatFinal = ("Demandez à votre enseignant(e) de vous aider")
        return resultatFinal

# Demande l'élève s'il désire des problèmes d'addition ou de multiplication
print("Ce programme affichera un test de 10 questions aléatoires")
operation = int(input("Insrivez 0 si vous voulez des problèmes d'addition et 1 pour des problèmes de multiplication : "))
while operation < 0 or operation > 1:
    operation = int(input("Vous devez insrire 0 pour des questions d'addition et 1 pour des question de multiplications : "))

# Apelle la fonction
resultatFinal, bonne_reponse = effectuezTest(operation)

# Afficher la réponse finale
print(("{0} réponse(s) correcte(s)").format(bonne_reponse))
print(resultatFinal)

