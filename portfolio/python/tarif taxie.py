def prixTaxe (distance_km,tarif,temps_attente_min):
    if tarif == "A":
        trajet_km=1.22
    elif tarif == "B":
        trajet_km=1.61
    elif tarif == "C":
        trajet_km=1.74
    else:
        print ("erreur")
    tarif = distance_km*trajet_km+4.40+temps_attente_min*38/60
    if tarif<8:
        tarif =8
    return tarif
    
    
print (round(prixTaxe(5,"A",0),2))
print (round(prixTaxe(5,"B",10),2))