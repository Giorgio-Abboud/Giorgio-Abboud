# Programme calcule la note finale

# Calcule la note finale
def noteFinale(devoirsMoyenne, partiel, examen):
    note_finale = (devoirsMoyenne*25/100)+(partiel*25/100)+(examen*50/100)
    return note_finale

# Demande pour les notes
devoirsMoyenne = float(input("Inscrivez la note moyenne de vos devoirs : "))
partiel = float(input("Inscrivez votre note partielle : "))
examen = float(input("Inscrivez votre not d'examen : "))

# Affiche les résultats
note_finale = noteFinale(devoirsMoyenne, partiel, examen)
print("Votre note finale est de {0}%".format(note_finale))
