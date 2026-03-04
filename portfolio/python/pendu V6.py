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
    vie = 6
    for i in range (len(choix)):
            tentative = tentative + "-"
    while tentative != choix and vie != 0:
        lettre = input("choisir une lettre : ")
        if lettre in choix:
            tentative2 = ""
            for i in range (len (choix)):
                if choix[i] == lettre:
                    tentative2 = tentative2 + lettre
                else:
                    tentative2 = tentative2 + tentative[i]
        else:
            vie = vie -1
        print ("voici vos vie :",vie )
        print (tentative)
        tentative = tentative2
    if tentative == choix:
        print ("BRAVO vous avais gagné :","rien")
    else:
        print ("PERDU :", choix)
    
main()