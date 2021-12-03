# ce programme transforme de livres et onces en kilogrammes

def convertEnKilos(livres, onces):
  "prend livres et onces et retourne kilogrammes"
  kilos = (livres * 16 + onces) * 0.02835
  return kilos
  
livres = float(input("Entrez le nombre de livres: "))
onces = float(input("Entrez le nombre d'onces: "))

kilos = convertEnKilos(livres, onces)
print(livres,"livres et",onces,"onces est",kilos,"kilogrammes.")

  
