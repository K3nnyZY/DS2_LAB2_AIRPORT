from flask import Flask, render_template, request
from graph import Graph
from node import Capital_Node
import folium
import pandas as pd
import os

grafo = Graph()

data = pd.read_csv("data/data.csv")

capitals = data.groupby('Origin').first().reset_index()

for index, capital in capitals.iterrows():
    node = Capital_Node(capital['Origin'])
    node.pos = index
    node.lat = capital['lat_st']
    node.long = capital['lng_st']
    grafo.country_list.append(capital['Origin'])
    grafo.vertex_list.append(node)


for index, info in data.iterrows():
    indexor = grafo.country_list.index(info["Origin"])
    indexdes = grafo.country_list.index(info["Destination"])
    ciudad_or = grafo.vertex_list[indexor]
    ciudad_des = grafo.vertex_list[indexdes]
    ciudad_or.connections.append(ciudad_des)
    ciudad_or.cost.append(round(info["distance"]))

map = folium.Map(location=[4.570868,-74.297333],zoom_start=6)
for index, location_info in data.iterrows():
    folium.Marker([location_info["lat_st"], location_info["lng_st"]], popup=location_info["Origin"], icon=folium.Icon(color="pink", icon="plane")).add_to(map)

# Guardamos el mapa en la carpeta requerida
directory = r"src/static"
Save = os.path.join(directory, "map.html")
map.save(Save)


grafo.dijkstra_shortest_path("LONDON", "PARIS")

print(grafo)
