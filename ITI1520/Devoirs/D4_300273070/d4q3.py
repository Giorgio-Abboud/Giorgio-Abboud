# Programme qui calcule les chiffres cubiques

# Création de la fonction
def cubique():

    # Demande pour les nombres et transforme le nombre en liste
    num = input("Inscrivez un nombre entié entre 100 et 499 : ")
    num_int = int(num)

    # Demande pour une autre nombre si le premier n'est pas entre 100 et 499
    while num_int > 499 or num_int < 100:
        num = input("Inscrivez un nombre entié entre 100 et 499 : ")
        num_int = int(num)   
    liste = [int(num_array) for num_array in num]

    # Calcule les nombres
    num1 = (liste[0]**3)
    num2 = (liste[1]**3)
    num3 = (liste[2]**3)

    # Vérifie si le nombre suit les exigences
    if (num1) + (num2) + (num3) == num_int:
        # Affiche le résultat
        print("{0} = {1}**3 + {2}**3 + {3}**3 = {4} + {5} + {6}".format(num_int, liste[0], liste[1], liste[2], num1, num2, num3))
    else:
        # Affiche le résultat
        print("Votre nombre entié inscrit n'est pas un nombre cube")

# Affiche le résultat
cubique()
