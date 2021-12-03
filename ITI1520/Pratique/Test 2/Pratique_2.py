### Question 1
##MaListe = [1]*100
##
##for i in range(2, 100):
##    for val in range(i*2, 100, i):
##        MaListe[val] = 0
##print(MaListe)
##
##for n in range(1, 100):
##    if MaListe[n]:
##        print(n, end=" ")

### Question 2
##def evalue_poly(x, coeffs):
##    coeffs.reverse()
##    value = 0
##    print(coeffs)
##    for i in range(len(coeffs)):
##        value += coeffs[i]*(x**i)
##    return value
##    
##print(evalue_poly(2,[1,2,3,4]))

### Question 3
##def maListe(s, cible):
##    mots = s.split(" ")
##    liste = []
##    value = 0
##    for i in range(len(mots)):
##        if mots[i] == cible:
##            liste.append(i)
##    if len(liste) == 0:
##        return False
##    return liste
##
##print(maListe("je suis avec mon pere, mon ami et mon voisin", "mon"))
##
##
##def index_inverse(s):
##    mots = s.split(" ")
##    dic = {}
##    for i in range(len(mots)):
##        mot = mots[i]
##        if mot not in dic:
##            dic[mot] = []
##            dic[mot].append(i)
##    return dic
##
##print(index_inverse("je suis avec mon pere, mon ami et mon voisin"))

# Question 4
def maFonction(s1, s2):
    if s1 == s2:
        return True
    else:
        return False

print(maFonction("mon", "mon"))

