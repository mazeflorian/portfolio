import random 
choix= ["pierre","feuille","ciseaux"]
while True:
    choix_ordi = random.choice (choix)
    choix_joueur = input(" choisir soit pierre, feuille, ciseaux ou fin pour terminé :")
    choix_joueur = choix_joueur.lower()
    if choix_joueur == "fin":
        break
    if choix_joueur==choix_ordi:
            print ("l'ordinateur a choisi :",choix_ordi,"le joueur a choisi :",choix_joueur,"(égalité)")
    elif choix_joueur == ("pierre") and choix_ordi == ("ciseaux") or choix_joueur == ("feuille") and choix_ordi == ("pierre") or choix_joueur == ("ciseaux") and choix_ordi == ("feuille"):
            print ("l'ordinateur a choisi :",choix_ordi,"le joueur a choisi :",choix_joueur,"(gagné)")
    else:
        print ("l'ordinateur a choisi :",choix_ordi,"le joueur a choisi :",choix_joueur,"(perdu)")


