import folium
import pandas

map = folium.Map(location=[51, 0], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="Map")

data = pandas.read_csv("/home/mark/Documents/Python_Course/App2Files/Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(el):
    if el < 1500:
        return 'green'
    elif el < 3000:
        return 'orange'
    else:
        return 'red'

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=8, popup=str(el)+"m", fill=True, fill_color=color_producer(el), color='grey', fill_opacity=0.8))

map.add_child(fg)
map.save("Map1.html")
