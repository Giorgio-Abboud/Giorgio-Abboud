# Programme qui prend une matrice et calcule la transposée

# Création d'une fonction
def somme_matrices(A, B):
    # Créer la matrice C qui calcule la somme
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A)):
            C[i].append(A[i][j]+B[i][j])
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
i = 0
while (i < m):
    j = 0
    B.append([])
    while j < n: 
        v = int(input("matrice["+str(i)+","+str(j) +"]="))
        B[i].append(v)
        j = j + 1
    i = i + 1

# Affiche la réponse
print(A, B)
print(somme_matrices(A, B))
