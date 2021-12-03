# Programme qui prend une chaine de charactères s et retourne une autre chaine codée

# Création de la fonction coder
def coder(s):
    sListe = []
    sListe = list(s)
    
    # Change l'ordre dans une paire consécutive
    s1 = ''.join(a+b for a, b in zip(s[1::2], s[::2]))

    if len(sListe)%2 != 0:
        s1 = s1 + s[len(s)-1]
        return s1
    else:
        return s1


# Demande pour un mot
s = str(input("Inscrivez un mot à encoder : "))

# Affiche la réponse
print(coder(s))
