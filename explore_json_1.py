#learning how to create a map of earthquakes in a day 
#map pulls up in internet browser

import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile) #.load converts json file to python file

json.dump(eq_data, outfile, indent=4) #make more readable

list_of_eqs = eq_data["features"]


mags,lons,lats = [],[],[] #creating 3 lists: magnitude, longitude, latitude
for eq in list_of_eqs:
    mag = eq['properties']['mag']  #use double [] to get to magnitude bc eq is a dictionary of dictionaries so
                                     #we have to call the key of the dictionary we're using and then the index we want  

    lon = eq['geometry']['coordinates'][0]
    lat =eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons, lat=lats)] #lon = expects a list of longitudes, same thing for lats = with latitude
my_layout = Layout(title = 'Global Eatthquakes')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename= 'global_earthquakes.html')