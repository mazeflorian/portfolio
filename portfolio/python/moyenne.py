#while = tant que

def main():
    total = 0
    compteur = 0
    x = input("saisissez un nombre positif et négatif (taper rient pour finir):")
    while x != "":
        nombre = float (x)
        total = total + nombre 
        compteur = compteur + 1
        x = input("saisissez un nombre positif et négatif (taper rient pour finir):")
    print (total / compteur)
main()