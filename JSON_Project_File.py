'''
Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African American over 10%
Map 3) Total price for in-state students living off campus over $50,000
'''

import json


infile = open('univ.json', 'r')
#outfile = open('readable_univ_dat.json', 'w')
school_data = json.load(infile) #converts to python file

#make univ more readable
#json.dump(school_data, outfile, indent = 4)
#print(len(school_data))

#create list of schools and other information for maps
uni = []

for i in school_data:
    conference = i['NCAA']["NAIA conference number football (IC2020)"]
    #print(conference)

    #messes up when using "or" ??
    #creating list of schools in correct conference
    if conference == 102:
        uni.append(i)
    elif conference == 107:
        uni.append(i)
    elif conference == 108:
        uni.append(i)
    elif conference == 127:
        uni.append(i)
    elif conference == 130:
        uni.append(i)
#print(len(uni))

enroll1,enroll2,enroll3, women_grad, enroll_aa, price_off_campus, lat1, lon1, lat2, lon2, lat3, lon3, hover_text1, hover_text2, hover_text3 = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
for i in uni:
    if i["Graduation rate  women (DRVGR2020)"] > 50:
        school_name1 =i['instnm']
        women_grad =i["Graduation rate  women (DRVGR2020)"]
        lon1.append(i["Longitude location of institution (HD2020)"])
        lat1.append(i["Latitude location of institution (HD2020)"])
        size = 0.0001* i["Total  enrollment (DRVEF2020)"]
        enroll1.append(size)
        
        hover_text1.append(f"{school_name1}, {women_grad}%")
    if i["Percent of total enrollment that are Black or African American (DRVEF2020)"] > 10:
        uni_name2 =i['instnm']
        enroll_aa =i["Percent of total enrollment that are Black or African American (DRVEF2020)"]
        lon2.append(i["Longitude location of institution (HD2020)"])
        lat2.append(i["Latitude location of institution (HD2020)"])
        hover_text2.append(f"{uni_name2}, {enroll_aa}%")
        size2 = 0.001*i["Total  enrollment (DRVEF2020)"]
        enroll2.append(size2)
    #for value in i["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]:
    try: 
        cost = int(i["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"])
    except TypeError:
        print("None")
    else:
        if cost > 50000:
            uni_name3 = i['instnm']
            lon3.append(i["Longitude location of institution (HD2020)"])
            lat3.append(i["Latitude location of institution (HD2020)"])
            hover_text3.append(f"{uni_name3}, {cost}")
            size3 = 0.001*i["Total  enrollment (DRVEF2020)"]
            enroll3.append(size3)
'''
print(len(uni_name1))
print(len(women_grad))
print(len(uni_name2))
print(len(enroll_aa))
print(len(uni_name3))
print(len(price_off_campus))
print(len(lon1))
print(len(lat1))
print(len(lon2))
print(len(lat2))
print(len(lon3))
print(len(lat3))
print(hover_text1)
print(hover_text2)
print(hover_text3)
'''

#graphing the maps
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

#creating map for women graduates
data1 = [
    {
        'type': 'scattergeo',     #dictionary of dictionaries #this is how Scattergeo expects the data!!!
        'lon': lon1, ##allows you to hover over a circle and get the lat and lon,
        'lat': lat1,
        'text': hover_text1,
        'marker' : { 
            'size':  enroll1, #creating a new list where we're multiplying each item in mags list by 5 and then adding it to a new list: LIST COMPREHENSION
                                            #makes all dots on map bigger
            'color': "blue",
            'colorscale': 'Viridis', #can pick from a list of different color scales
            'reversescale': True,  #decreasing 
            
        },
    }]

my_layout = Layout(title = 'Schools with More than 50% of Women Graduating')

fig = {'data': data1, 'layout': my_layout} 

offline.plot(fig, filename= 'graduating_women.html')

#map African American Enrollment
data2 = [
    {
        'type': 'scattergeo',     #dictionary of dictionaries #this is how Scattergeo expects the data!!!
        'lon': lon2, ##allows you to hover over a circle and get the lat and lon,
        'lat': lat2,
        'text': hover_text2,
        'marker' : { 
            'size':  enroll2, #creating a new list where we're multiplying each item in mags list by 5 and then adding it to a new list: LIST COMPREHENSION
                                            #makes all dots on map bigger
            'color': "blue",
            'colorscale': 'Viridis', #can pick from a list of different color scales
            'reversescale': True,  #decreasing 
            
        },
    }]

my_layout = Layout(title = '% of African American and Black Enrollment')

fig = {'data': data2, 'layout': my_layout} 

offline.plot(fig, filename= 'total enrollment.html')
#map for Price
data3 = [
    {
        'type': 'scattergeo',     #dictionary of dictionaries #this is how Scattergeo expects the data!!!
        'lon': lon3, ##allows you to hover over a circle and get the lat and lon,
        'lat': lat3,
        'text': hover_text3,
        'marker' : { 
            'size':  enroll3, #creating a new list where we're multiplying each item in mags list by 5 and then adding it to a new list: LIST COMPREHENSION
                                            #makes all dots on map bigger
            'color': "blue",
            'colorscale': 'Viridis', #can pick from a list of different color scales
            'reversescale': True,  #decreasing 
            
        },
    }]

my_layout = Layout(title = 'Price for In-State Students Off Campus, Above $50,000')

fig = {'data': data2, 'layout': my_layout} 

offline.plot(fig, filename= 'price.html')