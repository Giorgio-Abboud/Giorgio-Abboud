# Programme qui calcule le nombre d'occurrences d'une caractère c dans une chaine s

# Création de la fonction compteV1
def compteV1(s, c):
    # Compte les 'a'
    s = s.count(c)
    # Renvoie la réponse
    return s

# Création de la fonction compteV2
def compteV2(s, c):
    # Compte les 'a'
    c = 0
    for num in s:
        if num == 'a':
            c = c + 1
    # Renvoie la réponse
    return c

# Demande pour la chaine
s = str(input("Inscrivez une chaine de caractère : "))

# Affiche les réponses
print(compteV1(s, 'a'))
print(compteV2(s, 'a'))
