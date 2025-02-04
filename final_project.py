# -*- coding: utf-8 -*-
"""Final Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TEfPBo33PKMaM7rz5sA6ttpAvbw7cmVM

Final Project: Alison Ching, Anastasia Davis, Moller Myint, and Jessica Pinto
"""

# Facebook Social Connectedness Indices Choropleth
import folium
from pandas import DataFrame, Series
import pandas as pd
import requests
import sqlite3
import geopandas as gdp

# Read the country shape data from the designated source.
country_geo = requests.get("https://github.com/datasets/geo-countries/blob/master/data/countries.geojson?raw=true").json()
# Read the country data from the uploaded file, originally from https://data.humdata.org/dataset/social-connectedness-index.
country_data = pd.read_csv("facebook_data.tsv", delimiter='\t')

''' Unnecessary :`)
# Replacing the ISO2 country codes in country_data with country names.

# Read the ISO2 country code/country name pairs from ISO2 Country Codes.txt.
country_codes = pandas.read_csv("ISO2 Country Codes.txt", delimiter='\t')
# Create the database connection.
con = sqlite3.connect('countries.db')
# Create a cursor to navigate the database.
cur = con.cursor()
# Create tables for country codes and data
country_codes.to_sql("codes", con, if_exists='replace', index=False)
country_data.to_sql("data", con, if_exists='replace', index=False)
# Join the country names and data by the country codes.
cur = cur.execute("SELECT codes.Country, data.scaled_sci from codes JOIN data ON codes.Code=data.fr_loc where data.user_loc='US'")
# Create a DataFrame to hold the data.
df = pd.DataFrame(columns=["Country", "Score"])
# Insert the data from the table into the DataFrame.
for row in cur:
  df.loc[len(df.index)] = row
print(df)
'''
# Designate a user country for which to take scores.
user_country = 'US'
# Create DataFrame containing only scores from the designated country.
df = country_data.loc[country_data['user_loc']==user_country][['fr_loc', 'scaled_sci']]

# Create a new folium map.
m = folium.Map(location=[48, -102], zoom_start=3)

# Add the choropleth
folium.Choropleth(
    geo_data=country_geo,
    name="choropleth",
    data=df,
    columns=["fr_loc", "scaled_sci"],
    key_on="feature.properties.ISO_A2",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Facebook Connections to " + user_country,
    nan_fill_color="grey",
    bins=df['scaled_sci'].quantile([0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]),
).add_to(m)

folium.LayerControl().add_to(m)

m

# Economic Freedom Summary Indices Choropleth
import folium
from pandas import DataFrame, Series
import pandas as pd
import requests
import sqlite3
import geopandas as gdp
# Read the country shape data from the designated source.
country_geo = requests.get("https://github.com/datasets/geo-countries/blob/master/data/countries.geojson?raw=true").json()

# Read the country data from the uploaded file, originally from https://www.fraserinstitute.org/economic-freedom/dataset?geozone=world&page=dataset&min-year=2&max-year=0&filter=0.
country_data = pd.read_csv("economicdata2021-2021.csv")

df = country_data[['ISO Code', 'Economic Freedom Summary Index']]
# Create a new folium map.
m = folium.Map(location=[48, -102], zoom_start=3)

# Add the choropleth
folium.Choropleth(
    geo_data=country_geo,
    name="choropleth",
    data=df,
    columns=["ISO Code", "Economic Freedom Summary Index"],
    key_on="feature.properties.ISO_A3",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Economic Freedom Summary Indices",
    nan_fill_color="grey",
    bins=[3, 4, 5, 6, 7, 8, 8.6]
).add_to(m)

folium.LayerControl().add_to(m)

m

import pandas as pd
import matplotlib.pyplot as plt

# read the csv file scores.csv into dataframe
df = pd.read_csv('economicdata2021-2021.csv')

# plot scatter graph
x = df['Freedom to trade internationally']
y = df['Sound Money']
plt.scatter(x, y, color='green')
plt.title('Freedom to Trade Internationally vs Sound Money (by score 0-10)')
plt.xlabel('Freedom to Trade Internationally')
plt.ylabel('Sound Money')
plt.show()

# Top and Bottom 5 Countries' Economic Freedom Index Summaries

import pandas as pd
import matplotlib.pyplot as plt

# Get information from csv and convert it to DataFrame.
df = pd.read_csv("economicdata2021-2021.csv")

# Remove unecessary information from DataFrame.
df2 = df[["Countries", "Economic Freedom Summary Index"]]

# Create new dataframe with the lowest 5 countries and thir EFSIs
low5Index = df2.sort_values("Economic Freedom Summary Index")
countries = []
indices = []

# Add lowest 5 countries and their indices to individual arrays.
low5Index.head(5)
for i in range(0, 5):
  countries.append(low5Index['Countries'].loc[low5Index.index[i]])
  indices.append(low5Index['Economic Freedom Summary Index'].loc[low5Index.index[i]])

# Add highest 5 countries and their indices to indicvidual arrys.
top5Index = low5Index.tail(5)
for i in range(0,5):
  countries.append(top5Index['Countries'].loc[top5Index.index[i]])
  indices.append(top5Index['Economic Freedom Summary Index'].loc[top5Index.index[i]])

# Create a customize horizontal bar graph.
fig, ax = plt.subplots(figsize=(16,9))
colors = ['lightcoral', 'lightcoral', 'lightcoral', 'lightcoral', 'lightcoral', 'mediumaquamarine', 'mediumaquamarine', 'mediumaquamarine', 'mediumaquamarine', 'mediumaquamarine']
ax.barh(countries, indices, color = colors)

# Remove strong axes lines.
for s in ['top', 'bottom', 'left', 'right']:
  ax.spines[s].set_visible(False)

# Add x, y gridlines
ax.grid(color='navy', linestyle='-.', linewidth=0.5, alpha=0.2)

# Show top values
ax.invert_yaxis()

# Add annotation to bars
for i in ax.patches:
  plt.text(i.get_width()+0.2, i.get_y()+0.5, str(round((i.get_width()), 2)), fontsize=10, fontweight='bold', color='grey')

# Add plot information.
ax.set_title("Economic Freedom Summary Index of Top 5 and Bottom 5 Countries in the World", loc='left',)
plt.xlabel("Economic Freedom Summary Index")
plt.ylabel("Countries")
plt.show()

# Get the lowest 5 countries
low5c = countries[0:5]

# Get the lowest 5 EFSI
low5i = indices[0:5]

high5c = countries[5:10]
high5i = indices[5:10]
# Venezuela = VE, Zimbabwe = ZB, Syrian = SY, Sudan = SD, Yemen = YE

# Bottom 5 Countries based on Economic Freedom Index Summary and Their American Friendships

import csv
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

dfCountries = pd.read_csv("facebook_data.tsv", delimiter = '\t')
dfCountries.to_csv("countries.csv")

connection = sqlite3.connect('countries.cb')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS friendships")

cursor.execute("CREATE TABLE friendships(Top INTEGER NOT NULL, Loc1 TEXT NOT NULL, Loc2 TEXT NOT NULL, Friends INTEGER NOT NULL);")

file = open("countries.csv")

contents = csv.reader(file)

insert_records = "INSERT INTO friendships(Top, Loc1, Loc2, Friends) VALUES (?, ?, ?, ?)"
cursor.executemany(insert_records, contents)

friends = []
VEFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='VE'").fetchone()
friends.append(VEFriends)
ZWFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='ZW'").fetchone()
friends.append(ZWFriends[0])
SYFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='SY'").fetchone()
friends.append(SYFriends)
SDFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='SD'").fetchone()
friends.append(SDFriends)
YEFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='YE'").fetchone()
friends.append(YEFriends)

for i in range (0, len(friends)):
  if not friends[i]:
    friends[i] = 0

connection.close()

plt.figure(figsize=(13,5))
plt.scatter(low5i, friends, c = 'lightcoral', s = 150)
z = []
txt = ["VE", "ZW", "SY", "SD", "YE"]
for i in range(0,5):
  z.append(txt[i])

for i, txt in enumerate(z):
  plt.text(low5i[i], friends[i], txt)

plt.title("Number of Friends in the US VS. Economic Freedom Index Summary")
plt.xlabel("Economic Freedom Index Summary")
plt.ylabel("Number of Friends in the US")
plt.title("Bottom 5 Countries")
plt.suptitle("Number of Friends in the US VS. Economic Freedom Index Summary")
plt.show()

# Top 5 Countries based on Economic Freedom Index Summary and Their American Friendships

import csv
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

connection = sqlite3.connect('countries.cb')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS friendships")

cursor.execute("CREATE TABLE friendships(Top INTEGER NOT NULL, Loc1 TEXT NOT NULL, Loc2 TEXT NOT NULL, Friends INTEGER NOT NULL);")

dfCountries = pd.read_csv("facebook_data.tsv", delimiter = '\t')
dfCountries.to_csv("countries.csv")
file = open("countries.csv")

contents = csv.reader(file)

insert_records = "INSERT INTO friendships(Top, Loc1, Loc2, Friends) VALUES (?, ?, ?, ?)"
cursor.executemany(insert_records, contents)


# United States = US, NewZealand = NZ, Switzerland = CH, Hong Kong = HK, Singapore = SG
friends = []
USFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='US'").fetchone()
friends.append(USFriends[0])
NZFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='NZ'").fetchone()
friends.append(NZFriends[0])
CHFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='CH'").fetchone()
friends.append(CHFriends[0])
HKFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='HK'").fetchone()
friends.append(HKFriends[0])
SGFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='SG'").fetchone()
friends.append(SGFriends[0])

for i in range (0, len(friends)):
  if not friends[i]:
    friends[i] = 0

connection.close()



plt.figure(figsize=(13,5))
plt.scatter(high5i, friends, c = 'mediumaquamarine', s = 150)
z = []
txt = ["US", "NZ", "CH", "HK", "SG"]
for i in range(0,5):
  z.append(txt[i])

for i, txt in enumerate(z):
  plt.text(high5i[i], friends[i], txt)
plt.title("Top 5 Countries")
plt.suptitle("Number of Friends in the US VS. Economic Freedom Index Summary")
plt.xlabel("Economic Freedom Index Summary")
plt.ylabel("Number of Friends in the US")
plt.show()

# Alter top 5 countries to remove US
countries = []
indices = []

top5Index = low5Index.tail(6)

for i in range(0,6):
  countries.append(top5Index['Countries'].loc[top5Index.index[i]])
  indices.append(top5Index['Economic Freedom Summary Index'].loc[top5Index.index[i]])

high5c = countries
high5i = indices
high5c.remove("United States")
high5i.remove(8.14)

# Top 5 Countries based on Economic Freedom Index Summary and Their American Friendships
# Excludes American friends with themselves.


import csv
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

connection = sqlite3.connect('countries.db')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS friendships")

cursor.execute("CREATE TABLE friendships(Top INTEGER NOT NULL, Loc1 TEXT NOT NULL, Loc2 TEXT NOT NULL, Friends INTEGER NOT NULL);")

dfCountries = pd.read_csv("facebook_data.tsv", delimiter = '\t')
dfCountries.to_csv("countries.csv")
file = open("countries.csv")

contents = csv.reader(file)

insert_records = "INSERT INTO friendships(Top, Loc1, Loc2, Friends) VALUES (?, ?, ?, ?)"
cursor.executemany(insert_records, contents)


# United States = US, NewZealand = NZ, Switzerland = CH, Hong Kong = HK, Singapore = SG
friends = []
VEFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='US'").fetchone()
#friends.append(VEFriends[0])
ZWFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='NZ'").fetchone()
friends.append(ZWFriends[0])
SYFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='CH'").fetchone()
friends.append(SYFriends[0])
SDFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='HK'").fetchone()
friends.append(SDFriends[0])
YEFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 ='SG'").fetchone()
friends.append(YEFriends[0])
IEFriends = cursor.execute("SELECT Friends FROM friendships WHERE Loc1 = 'US' and Loc2 = 'IE'").fetchone()
friends.append(IEFriends[0])

for i in range (0, len(friends)):
  if not friends[i]:
    friends[i] = 0

connection.close()



plt.scatter(high5i, friends, c = 'mediumaquamarine', s = 150)
z = []
txt = ["NZ", "CH", "HK", "SG", "IE"]
for i in range(0,5):
  z.append(txt[i])

for i, txt in enumerate(z):
  plt.text(high5i[i], friends[i], txt)
plt.title("Top 5 Countries")
plt.suptitle("Number of Friends in the US VS. Economic Freedom Index Summary")
plt.xlabel("Economic Freedom Index Summary")
plt.ylabel("Number of Friends in the US")
plt.show()

#2021 Exports bar chart combined
import matplotlib.pyplot as plt
import pandas as pd

def main():
    #Reading data file using pandas
    EcoFreeDF = pd.read_csv("Economic_Freedom.csv")
    exportsDF = pd.read_csv("Exports2021.csv")

    countries = []
    indicies = []

    EcoFreeDF2 = EcoFreeDF[["Countries", "Economic Freedom Summary Index"]]
    exportsDF2 = exportsDF[["Country or Area", "Trade (USD)"]]

    exportsSorted = exportsDF2.sort_values(by = 'Trade (USD)', ascending = False)       #puts greatest values on top

    #add highest 5 countries and their indicies to individual arrays.
    top5Index = exportsSorted.head(5)
    for i in range(0,5):
        countries.append(top5Index["Country or Area"].loc[top5Index.index[i]])
        indicies.append(top5Index["Trade (USD)"].loc[top5Index.index[i]])

    #add lowest 5 countries and their indicies to individual arrays
    low5Index = exportsSorted.tail(5)
    for i in range (0,5):
        countries.append(low5Index["Country or Area"].loc[low5Index.index[i]])
        indicies.append(low5Index["Trade (USD)"].loc[low5Index.index[i]])

    # Create a customize horizontal bar graph1.
    colors = ['mediumaquamarine', 'mediumaquamarine', 'mediumaquamarine', 'mediumaquamarine', 'mediumaquamarine','salmon', 'salmon', 'salmon', 'salmon', 'salmon']

    fig, ax = plt.subplots(figsize=(16,9))

    ax.bar(countries, indicies, color = colors)


    #annotations at top of each bar
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005), fontsize=8, fontweight='bold', color='grey')

    # Add plot information.
    ax.set_title("2021 Exports", loc='center',)

    plt.xticks(rotation = 45)                   #rotates labels by 45 deg
    plt.xlabel("Countries")
    plt.ylabel("USD")
    plt.show()

main()

#2021 exports Bar chart separated
import matplotlib.pyplot as plt
import pandas as pd

def main():
    #Reading data file using pandas
    EcoFreeDF = pd.read_csv("Economic_Freedom.csv")
    exportsDF = pd.read_csv("Exports2021.csv")

    countries1 = []
    indicies1 = []
    countries2 = []
    indicies2 = []

    EcoFreeDF2 = EcoFreeDF[["Countries", "Economic Freedom Summary Index"]]
    exportsDF2 = exportsDF[["Country or Area", "Trade (USD)"]]

    exportsSorted = exportsDF2.sort_values(by = 'Trade (USD)', ascending = False)       #puts greatest values on top

    #add highest 5 countries and their indicies to individual arrays.
    top5Index = exportsSorted.head(5)
    for i in range(0,5):
        countries1.append(top5Index["Country or Area"].loc[top5Index.index[i]])
        indicies1.append(top5Index["Trade (USD)"].loc[top5Index.index[i]])

    #add lowest 5 countries and their indicies to individual arrays
    low5Index = exportsSorted.tail(5)
    for i in range (0,5):
        countries2.append(low5Index["Country or Area"].loc[low5Index.index[i]])
        indicies2.append(low5Index["Trade (USD)"].loc[low5Index.index[i]])

    # Create a customize horizontal bar graph1.
    colors1 = ['mediumaquamarine', 'mediumaquamarine', 'mediumaquamarine', 'mediumaquamarine', 'mediumaquamarine']
    colors2 = ['salmon', 'salmon', 'salmon', 'salmon', 'salmon']

    fig, ax1 = plt.subplots(figsize=(16,9))
    fig, ax2 = plt.subplots(figsize=(16,9))

    ax1.bar(countries1, indicies1, color = colors1)
    ax2.bar(countries2, indicies2, color = colors2)


    #annotations at top of each bar
    for p in ax1.patches:
        ax1.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005), fontsize=8, fontweight='bold', color='grey')

    #annotations at top of each bar
    for p in ax2.patches:
        ax2.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005), fontsize=8, fontweight='bold', color='grey')

    # Add plot information.
    ax1.set_title("2021 Highest Exports", loc='center',)
    ax2.set_title("2021 Lowest Exports", loc='center',)

    #plt.xticks(rotation = 45)                   #rotates labels by 45 deg
    plt.xlabel("Countries")
    plt.ylabel("USD")
    plt.show()

main()