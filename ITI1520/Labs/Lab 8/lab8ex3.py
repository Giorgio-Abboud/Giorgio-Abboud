# Programme qui prend une matrice et calcule la transposée

# Création d'une fonction
def produit_matrices(A, B):

    # Si le nombres de colonnes est supérieur au nombre rangées
    if (len(A)) < (len(B)):
        # Créer la matrice C qui calcule la somme
        C = [[0 for x in range(len(A))] for y in range(len(B))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k] * B[k][j]

    # Si le nombres de rangées est supérieur au nombre colonnes                
    elif (len(A)) > (len(B)):
        # Créer la matrice C qui calcule la somme
        C = [[0 for x in range(len(B))] for y in range(len(A))]
        for i in range(len(B)):
            for j in range(len(A[0])):
                for k in range(len(A)):
                    C[i][j] += B[i][k] * A[k][j]

    # Enlève la liste d'extra dans la matrice et retourne la matrice C
    if (m%p == 0) or (p%m == 0):
        del C[len(C)-1]
        return C
    else:
        return C

# Création de la matrice A
print("Matrice A")
A = []
m = int(input("Entrez le nombre de rangées : "))
n = int(input("Entrez le nombre de colonnes : "))
i = 0
while (i < m):
    j = 0
    A.append([])
    while j < n: 
        v = int(input("matrice["+str(i)+","+str(j) +"]="))
        A[i].append(v)
        j = j + 1
    i = i + 1

# Création de la matrice B
print("Matrice B")
B = []
p = int(input("Entrez le nombre de colonnes : "))
i = 0
while (i < n):
    j = 0
    B.append([])
    while j < p: 
        v = int(input("matrice["+str(i)+","+str(j) +"]="))
        B[i].append(v)
        j = j + 1
    i = i + 1

# Affiche la réponse
print(A, B)
print(produit_matrices(A, B))
