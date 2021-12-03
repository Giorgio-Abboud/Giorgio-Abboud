# Programme qui calcul s'il y a deux nombres consécutifs égaux dans une liste

# Fonction qui calcul s'il y a deux nombres consécutifs égaux dans la liste
def séquenceDeDeux(a):
    index = 0
    index1 = 1
    doublons = False
    for n in range(1, len(a)):
        if a[index] == a[index1]:
            doublons = True
            return doublons
        else:
            doublons = False
            index += 1
            index1 += 1
    return doublons

# Le programme demande a l'utilisateur de créer une liste
liste = str(input("Veuillez entrer une liste de valeurs séparées par des virgules :"))
séquence = liste.split(",")
a = []
for n in séquence:
    a.append(int(n))
 
# Appelle la fonction et affiche la réponse
doublons = séquenceDeDeux(a)
print(doublons)
