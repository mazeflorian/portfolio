#convertir des second en minute puis en heure
t = int(input(" choisir une second"))
#heure 
heure = t//3600
#reste heure
resteheure= t%3600
#minute
minute = resteheure//60
#second
second = resteheure%60
print (heure)
print (minute)
print (second)