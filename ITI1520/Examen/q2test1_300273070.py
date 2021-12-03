
# VOTRE NOM ET NUMÉRO D'ÉTUDIANT ICI
# Remplacer xxxxxx dans le fichier par votre NUMÉRO D'ÉTUDIANT

def danube(s):
     '''(str)->None
     Precondition: s contient seulement les lettres A,B,C,F
     '''
     #VOTRE CODE ICI
     A = danube.count("A")
     B = danube.count("B")
     C = danube.count("C")
     F = danube.count("F")
     total = A+B+C+F
     return A/total, B/total, C/total, F/total

print(danube(str(input("Inscrivez vos lettres : "))))
