# Programme qui calcul le montant de positives dans un liste

# Fonction qui calcul les positives dans un liste
def positive(a):
    index = 0
    p = 0

    # Boucle qui calcul le montant de positive dans la liste en utilisant len
    while index < (len(a)):
        if a[index] > 0:
            p = p + 1
        index = index + 1
    print(p)

# Le programme demande a l'utilisateur de créer le liste
numéro = str(input("Veuillez entrer une liste de valeurs séparées par des virgules :"))

# Le programme assure que les données dans la liste sont séparé
numéros = numéro.split(",")

# Créer la liste avec la variable A
a = []
for num in numéros:
    a.append(int(num))
 
# Appelle la fonction et affiche la réponse
positive(a)
