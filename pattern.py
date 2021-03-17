import csv
import plotly_express as px 

data = []
with open ("cleandata.csv")as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

headers = data[0]
planetdata = data[1:]        
headers[0] = "row_num"
print(len(headers), len(planetdata[0])) 

solarsystem_planetcount = {}
for planets in planetdata:
    if (solarsystem_planetcount.get(planets[11])):
        solarsystem_planetcount[planets[11]] += 1
    else:
        solarsystem_planetcount[planets[11]] = 1

max_solarsystem = max(solarsystem_planetcount, key = solarsystem_planetcount.get)
print(max_solarsystem)              

temp = list(planetdata)
for planet in temp:
    planetmass = planet[3]
    if(planetmass.lower() == "unknown"):
        planetdata.remove(planet)
        continue
    else:
        planetmass_value = planetmass.split(" ")[0] 
        planetmass_ref = planetmass.split(" ")[1] 
        if(planetmass_ref == "Jupiters"):
            planetmassvalue = float(planetmass_value) * 317.8 
            planet[3] = planetmassvalue
            planet_radius = planet[7]
            if(planet_radius.lower() == "unknown"):
               planetdata.remove(planet)
               continue
            else:
                planetradius_value = planet_radius.split(" ")[0] 
                planetradius_ref = planet_radius.split(" ")[1] 
                if(planetradius_ref == "Jupiter"):
                    planet_radius = float(planetradius_value) * 11.2
                    planet[7] = planet_radius

print(len(planetdata)) 

koi_planets = []
for planets in planetdata:
    if(max_solarsystem == planets[11]):
        koi_planets.append(planets) 

koi_planet_mass = []
koi_planet_name = []

for planets in koi_planets:
    koi_planet_name.append(planets[1]) 
    koi_planet_mass.append(planet[3]) 

graph = px.bar(x = koi_planet_name, y = koi_planet_mass)
graph.show() 

print(koi_planet_mass)  