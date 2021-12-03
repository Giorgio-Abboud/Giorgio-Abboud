# Programme qui prend une liste d'entiers et un entier n et renvoie le montant de ces nombres qui sont divisible par n

# Création de la fonction
def nombre_divisible(n, ch):

    # Création de la liste
    liste = list(eval(ch))
    listeResultat = []

    # Associer des valeurs au variables
    count = 0

    # Compte le nombres d'entiers divisible par n
    for i in liste:
        if i % n == 0:
            count = count + 1
    
    # Création de la deuxième liste a renvoyer
    listeResultat.append(count)

    # Retourner le résultat
    return listeResultat
    
# Demande pour les nombres
n = int(input("Inscrivez un entié qui prendra le rôle comme diviseur : "))
ch = input("Inscrivez une liste d'entiées séparées par des virgules : ")

# Appel la fonction
listeResultat = nombre_divisible(n, ch)
print("Le nombre d'éléments divisible par {0} dans la liste est : {1}".format(n, listeResultat[0]))

