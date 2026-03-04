import random
def motAleatoire ():
    mots =[]
    f = open ("French.txt", "r", encoding="utf-8")
    while True:
        ligne = f.readline()
        mot = ligne.strip()
        if mot == "":
            break
        mots.append(mot)
    choix=random.choice(mots)
    f.close()
    return choix 
def main ():
    print (motAleatoire())
main()
    