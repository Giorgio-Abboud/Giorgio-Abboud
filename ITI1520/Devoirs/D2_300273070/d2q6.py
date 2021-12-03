# Programme qui affiche un jeu de pierres entre deux enfants

# Donne une valeur au pierres et un maximum et minimum
pierre = 20
maxPierre = 5
minPierre = 1
est_valide = False

# Produit le jeu
while (pierre > 0):

    # Tour du premier joueur
    est_valide == False
    ramasseJ1 = int(input("Tour du premier joueur : "))
    
    if (ramasseJ1 >= minPierre) and (ramasseJ1 <= maxPierre) and (ramasseJ1 <= pierre):
        est_valide = True
    else:
        est_valide = False
        
    if est_valide == True:
        pierre = pierre - ramasseJ1
        print("Il y reste {0} pierres".format(pierre))

    else:
        print("Nombre invalide, vous devez ramasser entre 1 et 5 pierres, et vous ne pouvez pas ramasser plus qu'il y reste dans la pile")
        while est_valide == False:
            ramasseJ1 = int(input("Tour du premier joueur : "))
    
            if (ramasseJ1 >= minPierre) and (ramasseJ1 <= maxPierre) and (ramasseJ1 <= pierre):
                est_valide = True
            else:
                est_valide = False
        
            if est_valide == True:
                pierre = pierre - ramasseJ1
                print("Il y reste {0} pierres".format(pierre))

            else:
                print("Nombre invalide, vous devez ramasser entre 1 et 5 pierres, et vous ne pouvez pas ramasser plus qu'il y reste dans la pile")
            

    if (pierre == 0):
        print("Le premier joueur a gagné!")
        print("Jeu terminé")
        break

    # Tour du deuxième joueur
    est_valide == False
    ramasseJ2 = int(input("Tour du deuxième joueur : "))
    
    if (ramasseJ2 >= minPierre) and (ramasseJ2 <= maxPierre) and (ramasseJ2 <= pierre):
        est_valide = True
    else:
        est_valide = False
        
    if est_valide == True:
        pierre = pierre - ramasseJ2
        print("Il y reste {0} pierres".format(pierre))

    else:
        print("Nombre invalide, vous devez ramasser entre 1 et 5 pierres, et vous ne pouvez pas ramasser plus qu'il y reste dans la pile")
        while est_valide == False:
            ramasseJ2 = int(input("Tour du deuxième joueur : "))
    
            if (ramasseJ2 >= minPierre) and (ramasseJ2 <= maxPierre) and (ramasseJ2 <= pierre):
                est_valide = True
            else:
                est_valide = False
        
            if est_valide == True:
                pierre = pierre - ramasseJ2
                print("Il y reste {0} pierres".format(pierre))

            else:
                print("Nombre invalide, vous devez ramasser entre 1 et 5 pierres, et vous ne pouvez pas ramasser plus qu'il y reste dans la pile")

    if (pierre == 0):
        print("Le deuxième joueur a gagné!")
        print("Jeu terminé")
        break
