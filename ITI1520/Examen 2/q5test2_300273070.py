

# METTRE VOTRE NOM ET NUMÉRO D'ÉTUDIANT ICI
#
# En mettant votre nom ici, vous signez la déclaration d'intégrité de q4test2 
#Giorgio Abboud
#300273070

#########################
# QUESTION 5
#########################            
    
def tanganyika(L):
    '''(list of int)->list
    Precondition: len(L)>=1
    Cette fonction doit renvoyer une nouvelle liste Q. 

    >>> tanganyika([1,2,0,0,0,3,0])
    [1, 2, 0, 3, 0]
    >>> tanganyika([1,2,0,0,0,3,0,0,0,0])
    [1, 2, 0, 3, 0] 
    >>> tanganyika([0,0,1,0,2,0,0,0,3,0,0,0,0])
    [0, 1, 0, 2, 0, 3, 0]
    >>> tanganyika([1,2,0,3,0])
    [1, 2, 0, 3, 0]
    '''

    #VOTRE CODE ICI
    liste = list(eval(L))

    index = 0
    Q = []
    for i in liste:
        Q.append(i)


    for i in Q:
        if i == 0:
            while index < len(Q)-1:
                if Q[index] == Q[index + 1]:
                    del Q[index]
                else:
                    index = index + 1
    return Q
            

    
L = input("Inscrivez une des nombres séparer par des virgules : ")
print(tanganyika(L))
