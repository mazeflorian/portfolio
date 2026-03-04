debut = int(input("choisir un nombre début :"))
fin = int(input("choisir un nombre fin :"))
if debut > fin:
    print ("erreur")
else:
    for i in range(debut, fin+1):
        carre = i**2
        print (i,carre)