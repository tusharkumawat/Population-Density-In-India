import folium
import pandas as pd
from folium.plugins import MarkerCluster

# loading data
data = pd.read_csv("Population_India.csv")
lat = data['Latitude']
lon = data['Longitude']
population = data['Population_2011']

# creating base map
map = folium.Map(location=[20.5937,78.9629],tiles='CartoDB dark_matter',zoom_start=5)

# creating cluster
marker_cluster = MarkerCluster().add_to(map)

# color function
def color_change(population):
    if population<1000000:
        color='cyan'
    elif 1000000 <= population < 2000000:
        color='green'
    elif 2000000 <= population < 3000000:
        color='yellow'
    elif 4000000 <= population < 4000000:
        color='orange'
    else:
        color='red'
    return color

# adding marker
for lat, lon, population in zip(lat, lon, population):
    folium.CircleMarker(location=[lat, lon], radius=9, popup=str(population)+'m', fill_color=color_change(population),color='gray',fill_opacity=0.9).add_to(marker_cluster)



# saving map
map.save("map.html")
