# Programme qui affiche True ou False si la liste est positive our négative

# Création d'une fonction
def vérifChiffres(A, N):
    if A[N] >= 0:
        if N == -1:
            booly = True
        else:
            booly = vérifChiffres(A, N-1)

    else:
        booly = False
        
    return booly

# Demande pour une liste
A = input("Inscris une liste d'entiers : ")
A = list(eval(A))
N = (len(A)-1)

# Appèle la fonction
print(vérifChiffres(A, N))

