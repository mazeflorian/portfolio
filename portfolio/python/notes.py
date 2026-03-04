
nombre = int(input ("choisir un nombre de note :"))
tab =[0 for _ in range (nombre)]

for i in range (nombre):
    note = float(input(" choisir des notes :"))
    tab[i] = note

somme = 0
somme_min = tab[0]
somme_max = tab[0]

for i in range (nombre):
    somme = somme + tab[i]
    if tab[i] < somme_min:
        somme_min = tab[i]
    if tab[i] > somme_max:
        somme_max = tab[i]

print (tab)
print (somme)
print (somme_min)
print (somme_max)
print (somme/nombre)

