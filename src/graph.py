from node import Capital_Node  # Importamos la clase Capital_Node desde otro archivo
from typing import List, Dict  # Importamos los tipos de datos List y Dict desde la librería typing
import heapq  # Importamos la librería heapq para implementar la cola de prioridad


class Graph:
    """
    Clase que representa un grafo de ciudades con aristas ponderadas por la distancia entre ellas.
    """

    def __init__(self):
        """
        Constructor de la clase Graph.
        """
        self.vertex_list: List[Capital_Node] = []  # Lista de nodos (ciudades) del grafo
        self.country_list: List[str] = []  # Lista de países del grafo


    def dijkstra_shortest_path(self, start: str, finish: str) -> List[Capital_Node]:
        """
        Implementa el algoritmo de Dijkstra para encontrar el camino más corto entre dos ciudades en el grafo.

        Args:
            start (str): Nombre de la ciudad de origen.
            finish (str): Nombre de la ciudad de destino.

        Returns:
            List[Capital_Node]: Lista de nodos que representan el camino más corto desde la ciudad de origen a la ciudad de destino.
        """
        start_node = self.get_vertex(start)  # Obtenemos el nodo (ciudad) de origen
        finish_node = self.get_vertex(finish)  # Obtenemos el nodo (ciudad) de destino

        # Inicializamos los valores de la distancia más corta desde el origen hasta cada nodo del grafo
        shortest_path: Dict[Capital_Node, float] = {node: float('inf') for node in self.vertex_list}
        shortest_path[start_node] = 0

        # Diccionario que almacena el nodo anterior en el camino más corto para cada nodo del grafo
        previous_nodes: Dict[Capital_Node, Capital_Node] = {}

        # Cola de prioridad para seleccionar el nodo con la distancia más corta en cada iteración del algoritmo
        priority_queue = [(0, start_node)]

        while priority_queue:
            # Seleccionamos el nodo con la distancia más corta de la cola de prioridad
            current_cost, current_min_node = heapq.heappop(priority_queue)

            # Si ya se ha visitado el nodo con una distancia menor, pasamos al siguiente nodo en la cola de prioridad
            if current_cost > shortest_path[current_min_node]:
                continue

            # Iteramos sobre los nodos vecinos del nodo actual para actualizar las distancias más cortas
            for neighbor, cost in zip(current_min_node.connections, current_min_node.cost):
                tentative_cost = shortest_path[current_min_node] + cost
                if tentative_cost < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_cost
                    previous_nodes[neighbor] = current_min_node
                    heapq.heappush(priority_queue, (tentative_cost, neighbor))

            # Si hemos llegado al nodo de destino, terminamos el algoritmo
            if current_min_node == finish_node:
                break

        # Reconstruimos el camino más corto a partir del diccionario de nodos anteriores
        return self._reconstruct_path(previous_nodes, start_node, finish_node)


    def get_vertex(self, capital: str) -> Capital_Node:
        """
        Obtiene el nodo correspondiente a una ciudad a partir de su nombre.

        Args:
            capital (str): Nombre de la ciudad.

            Returns:
                Capital_Node: El nodo correspondiente a la ciudad especificada, o None si no se encuentra en el grafo.
            """
        for node in self.vertex_list:
            if node.capital == capital:
                return node
        return None


    def _reconstruct_path(self, previous_nodes: Dict[Capital_Node, Capital_Node], start_node: Capital_Node, finish_node: Capital_Node) -> List[Capital_Node]:
        """
        Reconstruye el camino más corto a partir del diccionario de nodos anteriores.

        Args:
            previous_nodes (Dict[Capital_Node, Capital_Node]): Diccionario que almacena el nodo anterior en el camino más corto para cada nodo del grafo.
            start_node (Capital_Node): Nodo de origen.
            finish_node (Capital_Node): Nodo de destino.

        Returns:
            List[Capital_Node]: Lista de nodos que representan el camino más corto desde el nodo de origen hasta el nodo de destino.
        """
        path = []
        current_node = finish_node
        while current_node != start_node:
            try:
                path.insert(0, current_node)
                current_node = previous_nodes[current_node]
            except KeyError:
                # Si no se puede encontrar el nodo anterior para un nodo en el camino más corto, entonces no hay camino posible
                return []
        path.insert(0, start_node)

        return path


    def __str__(self):
        """
        Representación en cadena de caracteres del grafo.

        Returns:
            str: Cadena de caracteres que representa el grafo.
        """
        res = ""
        for vertex in self.vertex_list:
            res += f"\nCapital origen:\n{vertex.capital} (Lat: {vertex.lat}, Long: {vertex.long})\n"
            res += f"Capitales destino:\n"
            for connection, cost in zip(vertex.connections, vertex.cost):
                res += f"\t{connection.capital}, costo: {cost} km\n"
        return res