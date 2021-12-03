# calcule le nombre minimal de monnaie que le cassier peut rendre

def numMonnaie(dollars):
  "prend le montant en dollars et retourne le nombre minimal de monnaies que le cassier peut rendre"
  cents=int(dollars*100) # transfome dollars en centimes
  
  quarters=cents//25 
  cents=cents%25
  #le restant en centimes apres les quarters sont deduits
    
  dimes=cents//10
  cents=cents%10
   
  nickels=cents//5
  pennies=cents%5
    
  min_num = quarters + dimes + nickels + pennies
  return min_num

dollars =  float(input("Entrez le montant en dollars: "))
    
print("Le nombre minimal de monnaies que le cassier peut rendre est:",numMonnaie(dollars))
