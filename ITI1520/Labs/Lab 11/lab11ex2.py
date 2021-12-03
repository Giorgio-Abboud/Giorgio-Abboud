# Programme qui copie une liste

# Création d'une fonction
def initListe(L, N):
    if N != -1:
        L.append(N)
        initListe(L, N-1)

    L.sort()
    return L

# Demande pour une liste
L = []
N = int(input("Inscris un nombre : "))
N = N - 1

# Appèle la fonction
print(initListe(L, N))

