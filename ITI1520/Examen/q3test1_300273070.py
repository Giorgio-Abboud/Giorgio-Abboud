
# VOTRE NOM ET NUMÉRO D'ÉTUDIANT ICI
# Remplacer xxxxxx dans le fichier par votre NUMÉRO D'ÉTUDIANT

def helper(s1,s2): 
     '''(str,str)->int
     Preconditions: len(s) est non nul et len(s)%3==0
     s1 et s2 sont des chaînes composées d'entiers positifs
     '''

     #VOTRE CODE ICI
     # Voir si les listes de nombres sont impaires
     # Calcule si pair
     if s1%2==0 and s2%2==0:
          resultat_s = s1+s2
     # Calcule si impair
     elif s1%2==1 and s2%2==1:
          resultat_s = s1+s2
     # Calcule si pair et impair
     elif s1%2==0 and s2%2!=0 or s1%2!=0 and s2%2==0:
          resultat_s = s1*s2
          
     return resultat_s

# Deamnder pour les nombres
num1 = input("Insrivez une liste de nombres separee par des virgules : ")
num11 = list(eval(num1))
while len(s1)%3!=0:
     num1 = input("Insrivez une liste de nombres separee par des virgules : ")
     num11 = list(eval(num1))

num2 = input("Insrivez une liste de nombres separee par des virgules : ")
num22 = list(eval(num2))
for i in num22:
    s2.append(int(i))
while len(s2)%3!=0:
     num2 = input("Insrivez une liste de nombres separee par des virgules : ")
     num22 = list(eval(num2))

resultat_s = helper(s1,s2)
print(resultat_s)
