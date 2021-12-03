# Programme qui retourne la longeur de la plus longue séquence dans une liste

# Création de la fonction
def sequenceMax(ch):

    # Création de la liste
    liste = list(eval(ch))

    # Association de valeurs au variables
    resultat = 1
    plusGrandResultat = 0
    seqFinale = liste[0]

    # Création de la boucle qui cherche pour la plus longue séquence
    for num in liste[1:]:
        
        # Cherche s'il y a un doublons et augemnte le résultat s'il y en as
        if num == seqFinale:
            resultat = resultat + 1

        # Enregistre le plus grand résultat si la plus longue séquence se termine
        else:
            if resultat > plusGrandResultat:
                plusGrandResultat = resultat
            seqFinale = num
            resultat = 1

    # Enregistre le plus grand résultat une dernière fois au cas que la séquence la plus longue est à la fin de la liste
    if resultat > plusGrandResultat:
                plusGrandResultat = resultat

    # Retrourne la valeur de la plus longue séquence        
    return plusGrandResultat
    
# Demande pour les nombres
ch = input("Inscrivez une liste d'entiées séparées par des virgules : ")

# Affiche le résultat
print(sequenceMax(ch))
