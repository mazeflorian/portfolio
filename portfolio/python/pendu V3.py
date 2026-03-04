import tracemalloc
import random
def chargerdictionnaire (mots):
    f = open ("French.txt", "r", encoding="utf-8")
    while True:
        ligne = f.readline()
        mot = ligne.strip()
        if mot == "":
            break
        mots.append(mot)
    f.close()
    return mots
def motAleatoire (mots):
    choix=random.choice(mots)
    return choix 
def main ():
    mots =[]
    chargerdictionnaire(mots)
    choix =(motAleatoire(mots))
    tentative = ""
    for i in range (len(choix)):
        tentative = tentative + "-"
    print (tentative)
main()

