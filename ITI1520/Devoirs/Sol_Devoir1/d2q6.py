def annéesEnSecondes(années): 
  secondes = années * 365.26 * 24 * 60 * 60
  return secondes

def secondesLumièreEnKm(secondesLumière): 
  distance = secondesLumière * 300000
  return distance

def distanceEntreÉtoiles(distanceAl1, distanceAl2):
 secLum1 = annéesEnSecondes( distanceAl1 )
 secLum2 = annéesEnSecondes( distanceAl2 )
 distKm1 = secondesLumièreEnKm( secLum1 )
 distKm2 = secondesLumièreEnKm( secLum2 )
 return(distKm1 + distKm2)

a =  float(input("Entrez un nombre d'anees lumiere: "))
s = annéesEnSecondes(a)
print("Le nombre des secondes est", s)

dist = secondesLumièreEnKm(s)
print("La distance est", dist, "km.")

d1 =  float(input("Entrez la distance de la première étoile, en années-lumière: "))
d2 =  float(input("Entrez la distance de la deuxième étoile, en années-lumière: "))
print("La distance entre les deux etoiles est", distanceEntreÉtoiles(d1, d2), "km") 
 
