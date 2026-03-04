lettre = input("choisir une lettre :")

listemois = ['janvier','février','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','décembre']

for mois in listemois:
    for carractere in mois:
        if carractere == lettre:
            print (mois)
