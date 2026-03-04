conteur = 0
for line in open ("C:/Users/Pc Portable/Desktop/python/access.log"):
    if "404" in line:
        conteur = conteur+1
        if conteur == 5:
            print (line)
            conteur=0
    else:
        conteur = 0