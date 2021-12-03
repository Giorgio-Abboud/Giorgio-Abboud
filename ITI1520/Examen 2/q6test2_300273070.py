# METTRE VOTRE NOM ET NUMÉRO D'ÉTUDIANT ICI
#
# En mettant votre nom ici, vous signez la déclaration d'intégrité de q4test2 
#Giorgio Abboud
#300273070

#########################
# QUESTION 6
#########################

def baikal(L):
    '''(list of int) -> bool
    Conditions préalables : len(L)>=2

    >>> baikal([4,5,3,0,-4])
    True
    >>> baikal([4,5,-7])
    False'''

    #VOTRE CODE ICI
    a, b, c, d= 0, 0, 0, 1

    index = 0
    resultat = True

    while index > len(L)-1:
        a, b = L[index], L[index+1]
        if a < b:
            c = b - a
            if c == d:
                resultat = True
            elif c != d:
                resultat = False
        else:
            c = a - b
            if c == d:
                resultat = True
            if c != d:
                resultat = False
                
        index += 1
        d += 1

        return resultat
    
L = input("Inscrivez une des nombres séparer par des virgules : ")
resultat = baikal(L)
print(resultat)
