caractère = input("choisir un caractère :")

alphabet = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#len = nombre de carracter / exemple len(afd4) --> 4
if len(caractère)>1:
    print ("erreur")

else:
    if ord(caractère)<ord("A") or ord(caractère)>ord("Z"):
        print("erreur")
    else:
        X = ord(caractère) - ord("A")
        y = (3*X+11) %26
        print (alphabet [y])