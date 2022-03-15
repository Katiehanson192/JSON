'''
Map 1) Graduation rate for Women is over 50%
Map 2) Percent of total enrollment that are Black or African American over 10%
Map 3) Total price for in-state students living off campus over $50,000
'''
import json
from textwrap import indent

infile = open('univ.json', 'r')
#outfile = open('readable_univ_dat.json', 'w')
school_data = json.load(infile) #converts to python file

#make univ more readable
#json.dump(school_data, outfile, indent = 4)
#print(len(school_data))

#create list of school
uni = []

for i in school_data:
    conference = i['NCAA']["NAIA conference number football (IC2020)"]
    #print(conference)

    #messes up when using "or" ??
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

uni_name1,uni_name2,uni_name3, women_grad, enroll_aa, price_off_campus = [],[],[],[],[],[]
for i in uni:
    if i["Graduation rate  women (DRVGR2020)"] > 50:
        uni_name1.append(i['instnm'])
        women_grad.append(i["Graduation rate  women (DRVGR2020)"])
    if i["Percent of total enrollment that are Black or African American (DRVEF2020)"] > 10:
        uni_name2.append(i['instnm'])
        enroll_aa.append(i["Percent of total enrollment that are Black or African American (DRVEF2020)"])

    #for value in i["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"]:
    try: 
        cost = int(i["Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"])
    except TypeError:
        print("None")
    else:
        if cost > 50000:
            uni_name3.append(i['instnm'])
            price_off_campus.append(cost)
    
print(len(uni_name1))
print(len(women_grad))
print(len(uni_name2))
print(len(enroll_aa))
print(len(uni_name3))
print(len(price_off_campus))


