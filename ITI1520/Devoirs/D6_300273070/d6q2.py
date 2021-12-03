# Programme qui affiche des étoiles et retorune la somme des éléments positives d'une liste

# Création d'une fonction
def etoile(n):
    print('*'*n)
    if n > 1:
        etoile(n-1)
    print('*'*n)

# Demande pour un entier
n = int(input("Inscris un entier non négatif : "))
while n < 0:
    n = int(input("Inscris un entier négatif : "))

# Appèle la fonction
etoile(n)

# Création d'une autre fonction
def sommeListePos_rec(l):
    if len(l) == 0:
        return 0
    num = l.pop()
    if num > 0:
        return num + sommeListePos_rec(l)
    return sommeListePos_rec(l)  
    
# Demande pour une liste
l = input("Insris une liste de nombres : ")
l = list(eval(l))

# Appèle la fonction
print(sommeListePos_rec(l))
