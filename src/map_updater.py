import pandas as pd
import folium
import os

class MapUpdater:

    def __init__(self, grafo) -> None:
        self.grafo = grafo

    def node_exists(self, node_data):
        for node in self.grafo.vertex_list:
            if node.capital == node_data:
                return True
        return False

    def add_marker(self, map, location_info, color, icon):
        folium.Marker(
            [location_info["lat_st"], location_info["lng_st"]],
            popup=location_info["Ciudad_Origen"],
            icon=folium.Icon(color=color, icon=icon),
        ).add_to(map)

    def add_polyline(self, map, node1, node2, color, weight, tooltip):
        folium.vector_layers.PolyLine(
            [(node1.lat, node1.long), (node2.lat, node2.long)],
            color=color,    
            weight=weight,
            tooltip=tooltip,
        ).add_to(map)

    def update_map(self, start: str, finish: str):
        if start == finish or not start or not finish:
            return

        if not self.node_exists(start) or (finish != "TODOS" and not self.node_exists(finish)):
            return

        vuelos = pd.read_csv('data/totalvuelos.csv')
        map = folium.Map(location=[4.570868, -74.297333], zoom_start=6)

        for index, location_info in vuelos.iterrows():
            if location_info["Ciudad_Origen"] == start:
                self.add_marker(map, location_info, "lightred", "plane")
            elif location_info["Ciudad_Origen"] == finish:
                self.add_marker(map, location_info, "lightgreen", "plane")
            else:
                self.add_marker(map, location_info, "pink", "plane")

        if finish == "TODOS":
            for node in self.grafo.vertex_list:
                if node.capital != start:
                    try:
                        path_list = self.grafo.short_path_list(start, node.capital)
                    except ValueError:
                        continue
                    for i in range(len(path_list) - 1):
                        node1, node2 = path_list[i], path_list[i+1]
                        if node2 in node1.connections:
                            weight = node1.cost[node1.connections.index(node2)]
                            self.add_polyline(map, node1, node2, "blue", 3, str(weight))
        else:
            try:
                path_list = self.grafo.short_path_list(start, finish)
            except ValueError:
                return
            for i in range(len(path_list) - 1):
                node1, node2 = path_list[i], path_list[i+1]
                if node2 in node1.connections:
                    weight = node1.cost[node1.connections.index(node2)]
                    self.add_polyline(map, node1, node2, "blue", 3, str(weight))

        directory = r"src/static"
        Save = os.path.join(directory, "map.html")
        map.save(Save)

