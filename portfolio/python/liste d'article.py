# .append (nom de l'ajout) = ajouter quelque chose a une liste
# immutable = int, float, string / mutable = liste 
def ajoute_liste (liste,article):
    if article in liste:
        return True
    else:
        liste.append (article)
        return False 


course = ["pain","lait","oeufs"]
art = input ("choisir un article :")
if ajoute_liste(course,art):
    print ("aucun article monquant")
else:
    print ("article ajouté")
print (course)