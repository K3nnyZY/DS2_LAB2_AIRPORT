import pandas as pd
import webbrowser
from map_updater import MapUpdater
from flask import Flask, render_template, request
from graph import Graph, Capital_Node

grafo = Graph()
vuelos = pd.read_csv('data/data.csv')

capitals = vuelos.groupby('Origin').first().reset_index()

for index, capital in capitals.iterrows():
    node = Capital_Node(capital['Origin'])
    node.pos = index
    node.lat = capital['lat_st']
    node.long = capital['lng_st']
    grafo.country_list.append(capital['Origin'])
    grafo.vertex_list.append(node)

for index, info in vuelos.iterrows():
    indexor = grafo.country_list.index(info["Origin"])
    indexdes = grafo.country_list.index(info["Destination"])
    origins = grafo.vertex_list[indexor]
    destinations = grafo.vertex_list[indexdes]
    origins.connections.append(destinations)
    origins.cost.append(round(info["distance"]))

map_updater = MapUpdater(grafo)
map_updater.update_map_with_removed_vertex()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Inicio.html')

@app.route('/continuar', methods=["GET", "POST"])
def continuar():
    return render_template('App.html')

@app.route('/datos', methods=["GET", "POST"])
def ciudades():
    ciudad1 = request.form['city-1']
    ciudad2 = request.form['city-2']

    map_updater.update_map(ciudad1, ciudad2)

    return render_template('App.html')

@app.route('/modify_vertex', methods=["POST"])
def modify_vertex():
    if request.method == 'POST':
        city_to_modify = request.form['city-modify']
        action = request.form['action']

        if action == 'remove':
            map_updater.remove_vertex(city_to_modify)
        elif action == 'restore':
            map_updater.restore_vertex(city_to_modify)

    return render_template('App.html')

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5005", 0)
    app.run(debug=True, port=5005)
