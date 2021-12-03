
'''
Je comprends l'importance de l'intégrité professionnelle dans mes études et ma future carrière
en ingénierie ou en informatique. Je certifie par la présente que j'ai effectué et que je ferai tous les travaux
sur cet examen entièrement par moi-même, sans aide extérieure ou utilisation de matériel non autorisé
sources d'informations. De plus, je ne fournirai pas d'aide aux autres.
'''

# LIRE LA DÉCLARATION CI-DESSUS
#
# METTRE VOTRE NOM ET NUMÉRO D'ÉTUDIANT ICI
#Giorgio Abboud
#300273070

# En mettant votre nom ici, vous signez la déclaration ci-dessus et
# accepter le TEST 2 (règles d'intégrité)

#########################
# QUESTION 4
#########################

def nyasa(L):
    '''list of str->int
    Précondition : len(L)>0 et L ne contient pas de mots identiques

    >>> nyasa(["rat", "war", "sol", "ads"])
    6
    >>> nyasa(["rat", "jazzy", "war", "solei", "pizza"])
    4
    >>> nyasa(["at", "jazz", "war", "solei"])
    0
    '''
##    #VOTRE CODE ICI
    p = 1
    for m in L:
        while p < len(L):
            if m == L[p]:
                del (L[p])
                p = p + 1
                
            else:
                p = p + 1
    print(L)

    
L = str(input("Insérez une liste de mots spéarer pas des virgules : "))
L = list(L.split(", "))
print(L)
nyasa(L)

