
# Giorgio Abboud - 300273070
# Vous remplacer xxxxxx dans le fichier par votre NUMÉRO D'ÉTUDIANT

def irtysh(n):
     '''(int)->bool or int
     Preconditions: n=1 ou n est un entier positif à 5 digits (chiffres)'''
     #VOTRE CODE ICI
     if n == 1:
          divisible = 0
          entier = int(input("Inscrivez un entier : " ))
          for i in range(1, entier+1):
               if entier%i==0:
                    divisible = divisible + 1
          if divisible%3==0:
               return True
          else:
               return False
     else:
          return (n//100)%10
     
n = int(input("Inscrivez une nombre : "))

print(irtysh(n))



          
 
