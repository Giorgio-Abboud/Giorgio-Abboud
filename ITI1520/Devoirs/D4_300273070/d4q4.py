#Question 4 - Devoir 4

def read_raw(file):
    '''str->list of str
    Renvoie une liste de chaînes qui ont été stockées dans un fichier.'''
    raw = open(file).read().splitlines()
    for i in range(len(raw)):
        raw[i]=raw[i].strip()
    return raw


def clean_up(l):
    '''list of str->list of str
    La fonction prend en entrée une liste de caractères.
    Elle renvoie une nouvelle liste contenant les mêmes caractères que l
    sauf que un de chaque caractère apparaissant un nombre impair de fois
    dans l est supprimé et tous les caractères * sont supprimés 

    >>> clean_up(['A', '*', '$', 'C', '*', '*', 'P', 'E', 'D', 'D', '#', 'D', 'E', 'B', '$', '#'])
    ['#', '#', '$', '$', 'D', 'D', 'E', 'E']

    >>> clean_up(['A', 'B', '*', 'C', '*', 'D', '*', '*', '*', 'E'])
    []
    '''


    clean_board=[]

    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI

    # Création et l'organisation de la liste clean_board
    liste = list(b)
    liste.sort()
    clean_board = liste

    # Supprime le charactère *
    for charactere in clean_board[0:]:
        if charactere == "*":
            clean_board.pop(clean_board.index(charactere))

    # Supprime un charactère dont son count est impair
    for i in clean_board[0:]:
        if clean_board.count(i) % 2 != 0:
            clean_board.pop(clean_board.index(i))

    # Retourne la liste finale
    return clean_board
    
def  is_rigorous(l):
    '''list of str->bool
    Renvoie True si chaque caractère de la liste apparaît exactement 2 fois ou si la liste est vide.
    Sinon, elle renvoie False. 
    
    Précondition: vous pouvez supposer que chaque élément de la liste apparaît un nombre pair de fois
    (c'est-à-dire que la liste est nettoyée par la fonction clean_up)
    >>>  is_rigorous(['E', '#', 'D', '$', 'D', '$', 'E', '#'])
    True
    >>>  is_rigorous(['A', 'B', 'A', 'A', 'A', 'B'])
    False
    '''
    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI

    clean_board = clean_up(1)
    count = 0
    
    for i in clean_board[0:]:
        if clean_board.count(i) / 2 == 1:
            count = count + 1

    if len(clean_board) == 0 or count == len(clean_board):
        is_rigorous = True
        return is_rigorous
    else:
        is_rigorous = False
        return is_rigorous
    
#programme principal
file=input("Entrer le nom du fichier: ")
file=file.strip()
b=read_raw(file)
print("\nAvant clean-up:\n", b)
b=clean_up(b)
print("\nAprès clean-up:\n", b)
if is_rigorous(b):
    print("\nCette liste est maintenant rigoureuse; elle n’a aucun * et elle a "+str(len(b))+" caractères.")
else:
    print("\nCette liste n’a aucun * mais n'est pas rigoureuse et a "+str(len(b))+" caractères.")
     
