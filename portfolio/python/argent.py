# choisir un montant en euros ---> Euros
Euros = float(input(" choisir une montant en euros :"))
# choisir une devise étrangère ---> devise 
devise =  input(" Entrez le nom de la devise :")
# choisir le taux de charge ---> USD
taux_change = float(input(" taux de charge :"))
# converti l'euros en une autre devise
resultat = round(Euros*taux_change,2)
# résultat final 
print (Euros,"euros =",resultat,devise)



