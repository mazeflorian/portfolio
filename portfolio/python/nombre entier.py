#choisir un nombre entier ---> entier 
entier = int(input("choisir un entier :"))
#devision euclidienne 
resultat = entier%2
#si resultat et = 0 le nombre et pair
if resultat==0:
    print ("ce nombre et pair")
#sinon le nombre et impair 
else:
    print ("ce nombre et impair")