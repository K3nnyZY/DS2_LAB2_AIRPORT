import folium
import pandas as pd
import webbrowser
from map_updater import MapUpdater
from flask import Flask, render_template, request
import os
from graph import Graph, Capital_Node

grafo = Graph()
vuelos = pd.read_csv('data/data.csv')


cities = vuelos.groupby('Origin').first().reset_index()


for index, capital in cities.iterrows():
    node = Capital_Node(capital['Origin'])
    node.pos = index
    node.lat = capital['lat_st']
    node.long = capital['lng_st']
    grafo.country_list.append(capital['Origin'])
    grafo.vertex_list.append(node)


for index, info in vuelos.iterrows():
    indexor = grafo.country_list.index(info["Origin"])
    indexdes = grafo.country_list.index(info["Destination"])
    ciudad_or = grafo.vertex_list[indexor]
    ciudad_des = grafo.vertex_list[indexdes]
    ciudad_or.connections.append(ciudad_des)
    ciudad_or.cost.append(round(info["distance"]))


map = folium.Map(location=[54.5260, 15.2551],zoom_start=4)
for index, location_info in vuelos.iterrows():
    folium.Marker([location_info["lat_st"], location_info["lng_st"]], popup=location_info["Origin"], icon=folium.Icon(color="pink", icon="plane")).add_to(map)

grafo.dijkstra_shortest_path("LONDON","PARIS")
print(grafo)

# # Guardamos el mapa en la carpeta requerida
# directory = r"src/static"
# Save = os.path.join(directory, "map.html")
# map.save(Save)
# #Servidor en Flask
# app = Flask(__name__)
# @app.route('/') 
# #Primera ejecución
# def index():
#     return render_template('pp.html')
# #Para pasar a la página de los mapas
# @app.route('/continuar', methods=["GET", "POST"])
# def continuar():
#     return render_template('index.html')
# @app.route('/datos', methods=["GET", "POST"])
# #Recolectar los datos
# def ciudades():
#     ciudad1 = request.form['city-1']
#     ciudad2 = request.form['city-2']
#     # Redibujar el mapa
#     map_updater = MapUpdater(grafo)
#     map_updater.update_map(ciudad1, ciudad2)
#     # Refrescar la pagina
#     return render_template('index.html')
# if __name__ == '__main__':
#     webbrowser.open("http://127.0.0.1:5000", 1)
#     app.run(debug=True)
