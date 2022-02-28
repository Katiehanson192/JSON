#making improvements on the map 
#hover box
#

import json

infile = open('eq_data_30_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile) #.load converts json file to python file

json.dump(eq_data, outfile, indent=4) #make more readable

list_of_eqs = eq_data["features"]


mags,lons,lats, hover_texts = [],[],[], []#creating 3 lists: magnitude, longitude, latitude
for eq in list_of_eqs:
    mag = eq['properties']['mag']  #use double [] to get to magnitude bc eq is a dictionary of dictionaries so
                                     #we have to call the key of the dictionary we're using and then the index we want  

    lon = eq['geometry']['coordinates'][0]
    lat =eq['geometry']['coordinates'][1]
    title = eq['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

print(mags[:10])
print(lons[:10])
print(lats[:10])

#Scattergeo = info overlaid on world map
#code that creates the map
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

data = [
    {'type': 'scattergeo',     #dictionary of dictionaries #this is how Scattergeo expects the data!!!
    'lon': lons, ##allows you to hover over a circle and get the lat and lon,
    'lat': lats,
    'text': hover_texts,
    'marker' : { 
        'size':  [5* mag for mag in mags], #creating a new list where we're multiplying each item in mags list by 5 and then adding it to a new list: LIST COMPREHENSION
                                           #makes all dots on map bigger
        'color': mags,  #mags = list of eqs
        'colorscale': 'Viridis', #can pick from a list of different color scales
        'reversescale': True,  #decreasing 
        'colorbar': {'title':'Magnitude'} #title of reversescale = mag. IDs which element is being color coded
    },
    }]


my_layout = Layout(title = 'Global Eatthquakes')

fig = {'data': data, 'layout': my_layout} 

offline.plot(fig, filename= 'global_earthquakes.html')