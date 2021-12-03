# calcule le nombre minimal de monnaies que le caissier peut rendre

dollars =  float(input("Entrez le montant en dollars: "))
    
cents=int(dollars*100) # transfome dollars en centimes

quarters=cents//25 
cents=cents%25
#le reste en centimes apres les quarters sont deduits
    
dimes=cents//10
cents=cents%10
   
nickels=cents//5
pennies=cents%5
    
min_num = quarters + dimes + nickels + pennies

print("Le nombre minimal de monnaies que le cassier peut rendre est:", min_num)
