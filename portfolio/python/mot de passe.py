import hashlib 


def contient_majuscule(mot_de_passe):
    maj= ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for c in mot_de_passe:
        if c in maj:
            return True
    return False
    
  
def contient_miniscule(mot_de_passe):
    mini=("abcdefghijklmnopqrstuvwxyz")
    for l in mot_de_passe:
        if l in mini:
            return True
    return False

def contient_chiffre(mot_de_passe):
    chiffre = ("1 2 3 4 5 6 7 8 9")
    for f in mot_de_passe:
        if f in chiffre:
            return True
    return False

def taille_ok (mot_de_passe):
    if len (mot_de_passe)< 13:
        return True
    else:
        return False 

def Validation_Mot_de_Passe(mot_de_passe):
    return contient_majuscule(mot_de_passe) and contient_miniscule(mot_de_passe) and contient_chiffre(mot_de_passe) and taille_ok(mot_de_passe)
    
def main():
    mot_de_passe = input("entrez votre mot de passe :")
    print (Validation_Mot_de_Passe(mot_de_passe))
    if Validation_Mot_de_Passe (mot_de_passe):
        mot_de_passe_hache = hashlib.sha256(mot_de_passe.encode()).hexdigest()
        print (mot_de_passe_hache)
    else:
        print ("erreur")
main()