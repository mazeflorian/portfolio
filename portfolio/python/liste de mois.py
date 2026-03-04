def liste_mois (fichier):
    mois = []
    for ligne in open (fichier, encoding="utf-8"):
        mois.append(ligne.strip())
    return mois

def liste_mois_sans_R (liste_mois):
    mois_sans_R =[]
    for mois in liste_mois:
        #cette ligne veut dire que si il y a un mois avec r il ajoute pas 
        if "r" not in mois:
            mois_sans_R.append(mois)
    return mois_sans_R
        
def main():
    mois=liste_mois("C:/Users/Pc Portable/Desktop/python/mois.txt")
    mois_sans_R = liste_mois_sans_R (mois)
    for mois in mois_sans_R:
        print(mois)
main()
        
