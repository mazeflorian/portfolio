nombre = int(input("choisir un nombre compris entre 1 à 10 :"))
if nombre >10:
    print ("erreur")
else:
    for i in range(1,nombre+1):
        for x in range(1,11):
            r= i*x
            print (i,"x",x,"=",r)