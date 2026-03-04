import random
carte = [["." for _ in range (5)]for _ in range (5)]

ligne_tresor = random.randint(1,5)
colone_tresor = random.randint(1,5)

def affiche_grille (grille):
    print ("  1 2 3 4 5")
    for i in range (5):
        print (i+1,end=" ")
        for j in range (5):
            print (grille[i][j],end=" ")
        print ()
    return 0


print ("bienvenue dans le jeux du trésor caché !!")
print ("un trésor se cache dans une grille de 5X5. les ligne et colone vont de 1 à 5.")
affiche_grille (carte)
trouver = False

while not trouver :
    ligne_user = int (input ("ligne 1 à 5 :"))
    colone_user = int (input ("colone 1 à 5 :"))
    if ligne_user == ligne_tresor and colone_user == colone_tresor:
        print ("gagné!!")
        trouver = True
    else:
        print ("rater")
        carte [ligne_user - 1][colone_user - 1] = "X"
        affiche_grille (carte)
        if ligne_user > ligne_tresor:
            print ("plus haut")
        elif ligne_user < ligne_tresor:
            print ("plus bas")
        if colone_user > colone_tresor:
            print ("plus à gauche")
        elif colone_user < colone_tresor:
            print ("plus à droit")
            