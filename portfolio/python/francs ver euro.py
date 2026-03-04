def francsVerseuro (f):
    euroconverti = f*6.555957
    return (euroconverti)


francseuro = float (input ( "choisir un montant en francs :"))
euro = francsVerseuro(francseuro)
print ("voila la somme en euro :",round(euro,2))