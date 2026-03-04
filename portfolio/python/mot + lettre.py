mot = input("choisir un mot :")
lettre = input("choisir une lettre :")

for caractere in mot:
    if caractere == lettre:
        print ("la lettre :",lettre, "est présente dans le mot :",mot)