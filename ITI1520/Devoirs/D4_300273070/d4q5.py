#Question 5 - Devoir 4
# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''

     donneur=[]
     autre=[]

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI


    # Donne une valeur pour m
     carte = 1


     # Boucle For pour déterminer la longuer du paquet restant
     for i in range(len(p)):


         # Détermine la longuer du paquet du joueur qui donne la carte
         if carte == 0:
             donneur.append(p[i])
             carte = 1

        # Détermine la longueur du paquet du joueur qui reçoit la carte
         elif carte == 1:
             autre.append(p[i])
             carte = 0

     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI


    # Créé la liste resultat pour les cartes restant
    resultat=[]


    # Détermine la longueur des cartes restant
    if len(l) < 2:
        return l


    # Fait en sorte que les cartes sont séparé
    l.sort()


    # Affiche les cartes
    l.append([''])


    # Donne une valeur pour t
    t = 1


    # Boucle while pour afficher le résultat et pour vérifier la valeur de t
    while t < len(l):

        if l[t-1][:-1] != l[t][:-1]:
            resultat.append(l[t-1])
            t += 1

        else:
            t += 2


    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''

    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI


    # Sépare les numéros des cartes puis affiche la réponse
    print('')
    print(' '.join(p))
    print('')

def entrez_position_valide(n):
    '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI

     
    # Demande à l'utilisateur qu'elle carte qu'il veut 
    nombre = int(input("Choissisez un de mes cartes entre 1 et " +str(n)+": "))


    # Si le nombre est valable alors la carte est pris
    if n >= nombre >= 1:
         return nombre

        
    # Sinon le programme re demande l'humain pour un nouveau nombre
    else:
        while True:
            nombre = int(input("Choissisez un de mes cartes entre 1 et " +str(n)+" : "))
            if n >= nombre >= 1:
                 return nombre
            else:
                continue

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI

    # Assure que le numéro de tour commence a 0 
     tour = 0

    # Boucle qui commence et termine le jeu
     while 1 >= tour >= 0:


         # Bouléenne pour déterminer si l'humain a gagné
         if len(humain) == 0:
             print("****************************************************")
             print("Vous avez plus de cartes")
             print("Félicitations! Vous avez gagné")

             # Brise le boucle
             break


        # Bouléenne pour déterminer si le robot a gagné
         elif len(donneur) == 0:
             print("****************************************************")
             print("J'ai plus de cartes")
             print("Vous avex perdu, Robot a gagné")

             # Brise la boucle
             break

        # Continue le boucle jusqu'à quelqu'un a gagné
         else:


             # Commence le jeu en montrant à l'humain ses cartes 
             if tour == 0:
                 print("***************************************************")
                 print("Votre tour.")
                 print("Votre main est:")
                 affiche_cartes(humain)
                 

                # Demande à l'humain de chosir une carte du robot
                 n = len(donneur)
                 print("J'ai",n,"cartes. Si 1 est ma première carte et "+str(n)+" pour ma dernière carte, qu'elle carte voulez-vous?")
                 resultat = entrez_position_valide(n)
                 

                # Détermine qu'elle numéro l'humain avez choisi puis affiche la réponse
                 if resultat == 1:
                     print("Vous avez choisi ma 1e carte.")
                 else:
                     print("Vous avez choise ma",str(resultat)+"e carte.")


                
                # Affiche si l'humain a créé une paire avec ses cartes
                 print("La voilà. C'est un", donneur[int(resultat)-1])
                 print("Avec",donneur[int(resultat)-1],"ajouté, votre main est:")


                # Le programme enlève la carte du Robot puis la donne à l'humain
                 humain.append(donneur[int(resultat)-1])
                 donneur.remove(donneur[int(resultat)-1])
                 affiche_cartes(humain)


                # Si oui alors le programme enlève le paire de ses mains
                 print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:")
                 humain =  elimine_paires(humain)
                 affiche_cartes(humain)
                 tour = 1
                 attend_le_joueur()

            # Bouléenne elif pour le tour du Robot
             elif tour == 1:
                 

                # Effectue le role du robot en choissisant un nombre random pour les cartes de l'humain
                 print("***************************************************")
                 print("Mon tour")
                 n = len(humain)
                 resultat = random.randint(1,n)

                 
                # Affiche la carte que le Robot avait pris
                 if resultat == 1:
                     print("J'ai pris votre 1e carte.")
                 else:
                     print("J'ai pris votre",str(resultat)+"e carte.")


                # Enlève la carte de l'humain puis la donne au Robot puis affiche la réponse
                 donneur.append(humain[int(resultat)-1])
                 humain.remove(humain[int(resultat)-1])
                 donneur = elimine_paires(donneur)
                 tour = 0
                 attend_le_joueur()
                
# programme principale
joue()

