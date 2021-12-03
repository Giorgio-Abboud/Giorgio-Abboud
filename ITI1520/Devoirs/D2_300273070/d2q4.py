# Programme qui incrémente la valeure de n et décrémente la valeure de p

# Demande pour la valeure de n et p
n = int(input("Inscrivez la valeure de n : "))
p = int(input("Inscrivez la valeure de p : "))

# Cherche une autre valeur pour p si c'était 0
while p <= 0:
    print("La valeur de p ne peut pas être nulle ou un nombre négatif")
    p = int(input("Inscrivez la valeure de p : "))

# Affiche et incrémentant la valeur de n tant qu’elle reste inférieure à celle de p
print("Les valeurs de n inférieurs à p sont:")
for inferieure in range(n, p):
    print(inferieure)

# Boucle qui décrémente la valeur de p et affichant sa valeur si elle est impaire
print("Les valeurs de p impaires sont:")
for impaire in reversed(range(n, p)):
    if (impaire % 2 != 0):
        print(impaire)     
