total = 0
num = 0
 
print ("saisisser -1 pour ne plus saisir de nombres")
while True:
    if num == -1:
        break
    total = total + num
    num = float (input("saisissez un nombre positif :"))
print ("somme :", total)