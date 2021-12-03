# Programme qui prend une matrice et calcule la transposée

# Création d'une fonction
def transpose(A):
    # Demande pour la matrice
    r = int(input("Entrez le nombre de rangées : "))
    c = int(input("Entrez le nombre de colonnes : "))

    # Insère les nombres la matrice A
    i = 0
    while (i < r):
        j = 0
        A.append([])
        while j < c: 
            v = int(input("matrice["+str(i)+","+str(j) +"]="))
            A[i].append(v)
            j = j + 1
        i = i + 1

    # Création de la deuxième matrice AT transposée
    colonne = len(A[0])
    rangees = len(A)
    
    AT = []
    for j in range(colonne):
        rangee = []
        for i in range(rangees):
            rangee.append(A[i][j])
        AT.append(rangee)

    # Retourne les matrices
    return A, AT

# Création de la matrice A
A = []

# Affiche la réponse
A, AT = transpose(A)
print(A)
print(AT)
