notes = [
    [12,15,14,9],
    [10,18,11,13],
    [16,14,19,17]
]
for ligne in range (3):
    somme =0
    for colonne in range (4):
        somme = somme + notes[ligne][colonne]
    moyenne_eleve = somme / 4
    print ("moyenne éléve :",moyenne_eleve)
    
    
somme=0 
    
for ligne in range (3):
    for colonne in range (4):
        somme = somme + notes[ligne][colonne]
moyenne = somme / 12
print ("moyenne général :",moyenne)
    