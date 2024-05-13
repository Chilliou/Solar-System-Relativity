# Python program to read
# json file
AVO = 6.67408e-11
 
import json
from Planet import Planet
 
# Opening JSON file
f = open('planetes.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
for i in data:
    print(data[i]['masse'])
 
print(data['Terre']['masse'])

F = AVO * ((data['Soleil']['masse']*data['Terre']['masse'])/data['Terre']['distance_soleil'] **2)
print(F)


print(data['Soleil'])
list_distance = []
for planet in data:
    if(planet != "Soleil"):
        list_distance.append(data[planet]["distance_soleil"])
list_distance.sort()

print(list_distance)
for planet in data:
    valeur = float(data[planet]['distance_soleil'])/min(list_distance)
    print(f"La valeur pixel de la distance : {valeur}")


list_planet = []
for planet in data:
    d = data[planet]
    dt_soleil = float(d['distance_soleil'])/min(list_distance)
    planet_actuel = Planet(planet, d["masse"], d["rayon"], d["vitesse"], dt_soleil, d["rgb"])
    list_planet.append(planet_actuel)

# Closing file

for p in list_planet:
    print(p)
f.close()