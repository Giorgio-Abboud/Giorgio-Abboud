def effaceTableau (tab):
   '''
   (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
    # a completer
    
   # retourne rien
   for i in tab:
      for j in i:
         tab = '-'
      
def verifieGagner(tab):  
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''

    # a completer
    
    # Voir si le jour X ou O a gagné horizontalement
    a = testLignes(tab)
    if a:
       if a == 'X':
          print("Joueur X a gagné!")
          return True
       elif a == 'O':
          print("Joueur O a gagné!")
          return True
         
    # Voir si le jour X ou O a gagné verticalement
    b = testCols(tab)
    if b:
       if b == 'X':
          print("Joueur X a gagné!")
          return True
       elif b == 'O':
          print("Joueur O a gagné!")
          return True

    # Voir si le jour X ou O a gagné diagonalement
    c = testDiags(tab)
    if c:
       if c == 'X':
          print("Joueur X a gagné!")
          return True
       elif c == 'O':
          print("Joueur O a gagné!")
          return True

    # Voir si personne a gagné
    d = testMatchNul(tab)
    if d:
       print("Personne à gagné")
       return True
    else:
       return False
 
def testLignes(tab):
   ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer
   
   # Voir si le jour X a gagné horizontalement
   if tab[0] == ['X','X','X'] or tab[1] == ['X','X','X'] or tab[2] == ['X','X','X']:
      return 'X'
   # Voir si le jour O a gagné horizontalement
   elif tab[0] == ['O','O','O'] or tab[1] == ['O','O','O'] or tab[2] == ['O','O','O']:
      return 'O'
   # Voir s'il y a aucun gagnant
   else:
      return '-'
  
def testCols(tab):
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer

   # Voir si le jour X a gagné verticalement
   if tab[0][0] == 'X' and tab[1][0] == 'X' and tab[2][0] == 'X':
      return 'X'
   elif tab[0][1] == 'X' and tab[1][1] == 'X' and tab[2][1] == 'X':
      return 'X'
   elif tab[0][2] == 'X' and tab[1][2] == 'X' and tab[2][2] == 'X':
      return 'X'
   # Voir si le jour O a gagné verticalement
   elif tab[0][0] == 'O' and tab[1][0] == 'O' and tab[2][0] == 'O':
      return 'O'
   elif tab[0][1] == 'O' and tab[1][1] == 'O' and tab[2][1] == 'O':
      return 'O'
   elif tab[0][2] == 'O' and tab[1][2] == 'O' and tab[2][2] == 'O':
      return 'O'
   # Voir s'il y a aucun gagnant
   else:
      return '-'

   
def testDiags(tab):
   ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   # a completer

   # Voir si le jour X a gagné verticalement
   if tab[0][0] == 'X' and tab[1][1] == 'X' and tab[2][2] == 'X':
      return 'X'
   elif tab[0][2] == 'X' and tab[1][1] == 'X' and tab[2][0] == 'X':
      return 'X'
   # Voir si le jour O a gagné verticalement
   elif tab[0][0] == 'O' and tab[1][1] == 'O' and tab[2][2] == 'O':
      return 'O'
   elif tab[0][2] == 'O' and tab[1][1] == 'O' and tab[2][0] == 'O':
      return 'O'
   # Voir s'il y a aucun gagnant
   else:
      return '-'

  
  
def testMatchNul(tab):
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
   * Si on ne trouve pas de '-' dans la matrice, retourne True. 
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer

   # Voir s'il y a un espace vide
   if tab[0][0] != '-' and tab[0][1] != '-' and tab[0][2] != '-' and tab[1][0] != '-' and tab[1][1] != '-' and tab[1][2] != '-' and tab[2][0] != '-' and tab[2][1] != '-' and tab[2][2] != '-':
      return True
   else:
      return False
   
