from graph import Graph
from node import Capital_Node
import pandas as pd

grafo = Graph()

data = pd.read_csv("data\data.csv")

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


grafo.Floyd_Warshall()

print(grafo)