import pandas as pd
import folium
import os
from graph import Graph
from node import Capital_Node

class MapUpdater:
    """
    Clase MapUpdater que se encarga de actualizar un mapa de Folium con marcadores y líneas 
    que representan vuelos entre ciudades, usando información de un grafo de nodos.
    """

    def __init__(self, grafo: Graph) -> None:
        """
        Constructor de la clase MapUpdater.

        Args:
        - grafo: objeto Grafo que contiene información sobre los nodos del grafo y sus conexiones.
        """
        self.grafo = grafo


    def node_exists(self, node_data):
        """
        Método que verifica si un nodo con la capital indicada existe en el grafo.

        Args:
        - node_data: str que indica la capital de la ciudad.

        Returns:
        - bool que indica si el nodo existe o no en el grafo.
        """
        for node in self.grafo.vertex_list:
            if node.capital == node_data:
                return True
        return False


    def add_marker(self, map, location_info, color, icon):
        """
        Método que agrega un marcador al mapa de Folium.

        Args:
        - map: objeto Map de Folium en el que se agregará el marcador.
        - location_info: diccionario que contiene información sobre la ubicación del marcador.
        - color: str que indica el color del ícono del marcador.
        - icon: str que indica el tipo de ícono del marcador.
        """
        folium.Marker(
            [location_info["lat_st"], location_info["lng_st"]],
            popup=location_info["Origin"],
            icon=folium.Icon(color=color, icon=icon),
        ).add_to(map)


    def add_polyline(self, map:folium, node1:Capital_Node, node2:Capital_Node, color:folium, weight:folium, tooltip):
        """
        Método que agrega una línea al mapa de Folium.

        Args:
        - map: objeto Map de Folium en el que se agregará la línea.
        - node1: objeto Nodo que indica el inicio de la línea.
        - node2: objeto Nodo que indica el final de la línea.
        - color: str que indica el color de la línea.
        - weight: int que indica el grosor de la línea.
        - tooltip: str que indica el texto que aparecerá cuando se pase el mouse sobre la línea.
        """
        folium.vector_layers.PolyLine(
            [(node1.lat, node1.long), (node2.lat, node2.long)],
            color=color,    
            weight=weight,
            tooltip=tooltip,
        ).add_to(map)

 
    def update_map(self, start: str, finish: str):
        """
        Método que actualiza el mapa de Folium con los marcadores y líneas correspondientes.

        Args:
        - start: str que indica la capital de la ciudad de origen de los vuelos a representar en el mapa.
        - finish: str que indica la capital de la ciudad de destino de los vuelos a representar en el mapa,
        o la cadena "TODOS" para representar todos los vuelos que parten de la ciudad de origen.
        """
        if start == finish or not start or not finish:
            return

        if not self.node_exists(start) or (finish != "TODOS" and not self.node_exists(finish)):
            return

        vuelos = pd.read_csv('data/data.csv')
        map = folium.Map(location=[4.570868, -74.297333], zoom_start=6)

        for _, location_info in vuelos.iterrows():
            if location_info["Origin"] == start:
                self.add_marker(map, location_info, "lightred", "plane")
            elif location_info["Origin"] == finish:
                self.add_marker(map, location_info, "lightgreen", "plane")
            else:
                self.add_marker(map, location_info, "pink", "plane")

        if finish == "TODOS":
            for node in self.grafo.vertex_list:
                if node.capital != start:
                    path_list = self.grafo.dijkstra_shortest_path(start, node.capital)
                    for i in range(len(path_list) - 1):
                        node1, node2 = path_list[i], path_list[i+1]
                        if node2 in node1.connections:
                            weight = node1.cost[node1.connections.index(node2)]
                            self.add_polyline(map, node1, node2, "blue", 3, str(weight))
        else:
            path_list = self.grafo.dijkstra_shortest_path(start, finish)
            for i in range(len(path_list) - 1):
                node1, node2 = path_list[i], path_list[i+1]
                if node2 in node1.connections:
                    weight = node1.cost[node1.connections.index(node2)]
                    self.add_polyline(map, node1, node2, "blue", 3, str(weight))

        directory = r"app/static"
        Save = os.path.join(directory, "map.html")
        map.save(Save)
