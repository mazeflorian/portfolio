#import time --> pour mesurer le temps
#import tracemalloc -->pour mesurer la mémoire (tracemalloc start()) (tracemalloc.stop())
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
    print (motAleatoire(mots))
main()
    