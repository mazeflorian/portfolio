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
    print(choix)
    tentative = ""
    lettre = input("choisir une lettre : ")
    tentative2 = ""
    for i in range (len(choix)):
        tentative = tentative + "-"
    for i in range (len (choix)):
        choix [i]
        if choix[i] == lettre:
            tentative2 = tentative2 + lettre
        else:
            tentative2 = tentative2 + "-"
    print (tentative2)
    
main()

