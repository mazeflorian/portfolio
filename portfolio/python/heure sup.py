#def calculPaie (heure,taux_horaire=11.88): marche aussi pas besoin de métre dans le print 
def calculPaie (heure,taux_horaire):
    if heure <= 35:
        salaire = heure*taux_horaire
    elif heure <= 43:
        #+ 25%
        salaire = 35*taux_horaire+(heure-35)*taux_horaire*1.25
    else:
        #+ 50%
        salaire = 35*taux_horaire+8*taux_horaire*1.25+(heure-43)*taux_horaire*1.5 
    return salaire


print (round(calculPaie (35,11.88),2))
print (round(calculPaie (45,11.88),2))
print (round(calculPaie (55,11.88),2))
