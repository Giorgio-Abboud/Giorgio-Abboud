# Programme qui calcule le nombre minimum de pièces nécéssaires

# Demande pour les total d'argent
total = float(input("Inscrivez le nombre total d'argent : "))

# Calcule le nombre de monnaie à remettre
total_fois_cent = total*100
monnaieQuarters = total_fois_cent//25
monnaieDimes = (total_fois_cent%(monnaieQuarters*25))//10
monnaieNickels = (total_fois_cent%(monnaieQuarters*25+monnaieDimes*10))//5
monnaiePennies = (total_fois_cent%(monnaieQuarters*25+monnaieDimes*10+monnaieNickels*5))//1
piecesTotal = int(monnaieQuarters)+int(monnaieDimes)+int(monnaieNickels)+int(monnaiePennies)

# Affiche la réponse
print("Le caissier remettra un minimum de {0} pièces de monnaie".format(piecesTotal))
