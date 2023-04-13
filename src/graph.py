from node import Capital_Node
from typing import List, Dict

class Graph:
    """
    Clase que representa un grafo dirigido ponderado. Utiliza la implementación del algoritmo de Dijkstra para
    encontrar los caminos más cortos entre nodos.
    """

    def __init__(self):
        """
        Inicializa un nuevo grafo vacío.
        """
        self.vertex_list: List[Capital_Node] = []  # Lista de nodos del grafo
        self.country_list: List[str] = []  # Lista de nombres de los países correspondientes a cada nodo


    def dijkstra_shortest_path(self, start: str, finish: str) -> List[Capital_Node]:
        """
        Método que calcula la ruta más corta entre dos nodos utilizando el algoritmo de Dijkstra.

        Args:
        - start: str que indica la capital de la ciudad de origen.
        - finish: str que indica la capital de la ciudad de destino.

        Returns:
        - Una lista de objetos Capital_Node que representa la ruta más corta entre el nodo de origen y el nodo de destino.
        """
        unvisited_nodes = list(self.vertex_list)
        shortest_path: Dict[Capital_Node, float] = {node: float('inf') for node in unvisited_nodes}
        previous_nodes: Dict[Capital_Node, Capital_Node] = {}

        shortest_path[self.get_vertex(start)] = 0

        while unvisited_nodes:
            current_min_node = min(unvisited_nodes, key=lambda node: shortest_path[node])
            neighbors = current_min_node.connections

            for neighbor in neighbors:
                tentative_cost = shortest_path[current_min_node] + current_min_node.cost[current_min_node.connections.index(neighbor)]
                if tentative_cost < shortest_path.get(neighbor, float('inf')):
                    shortest_path[neighbor] = tentative_cost
                    previous_nodes[neighbor] = current_min_node

            unvisited_nodes.remove(current_min_node)
            if current_min_node == self.get_vertex(finish):
                break

        return self._reconstruct_path(previous_nodes, start, finish)


    def get_vertex(self, capital: str) -> Capital_Node:
        """
        Método que devuelve el objeto Capital_Node correspondiente a la capital dada.

        Args:
        - capital: str que indica la capital de la ciudad.

        Returns:
        - Un objeto Capital_Node correspondiente a la capital dada.
        """
        for node in self.vertex_list:
            if node.capital == capital:
                return node
        return None


    def _reconstruct_path(self, previous_nodes: Dict[Capital_Node, Capital_Node], start: str, finish: str) -> List[Capital_Node]:
        """
        Método auxiliar para reconstruir la ruta más corta a partir de los nodos previos.

        Args:
        - previous_nodes: Diccionario que contiene los nodos previos en la ruta.
        - start: str que indica la capital de la ciudad de origen.
        - finish: str que indica la capital de la ciudad de destino.

        Returns:
        - Una lista de objetos Capital_Node que representa la ruta más corta entre el nodo de origen y el nodo de destino.
        """
        shortest_path_list = []
        current_node = self.get_vertex(finish)
        while current_node != self.get_vertex(start):
            try:
                shortest_path_list.insert(0, current_node)
                current_node = previous_nodes[current_node]
            except KeyError:
                return []
        shortest_path_list.insert(0, self.get_vertex(start))

        return shortest_path_list
    

    def remove_vertex(self, capital: str) -> None:
        """
        Elimina un vértice del grafo.

        Args:
            capital (str): La capital de la ciudad a eliminar del grafo.

        Returns:
            None

        Raises:
            ValueError: Si no se encuentra la capital en el grafo.
        """
        vertex_to_remove = self.get_vertex(capital)
        if vertex_to_remove is None:
            raise ValueError(f"Capital '{capital}' not found in graph.")

        # Remove connections to the vertex in other vertices
        for vertex in self.vertex_list:
            if vertex_to_remove in vertex.connections:
                connection_index = vertex.connections.index(vertex_to_remove)
                vertex.connections.pop(connection_index)
                vertex.cost.pop(connection_index)

        # Remove the vertex from vertex_list
        self.vertex_list.remove(vertex_to_remove)


    def restore_vertex_connections(self, capital: str, connections: List[Capital_Node], costs: List[float]) -> None:
        """
        Restaura las conexiones de un vértice eliminado previamente.

        Args:
            capital (str): La capital de la ciudad del vértice al que se restaurarán las conexiones.
            connections (List[Capital_Node]): La lista de nodos a los que el vértice restaurado estará conectado.
            costs (List[float]): La lista de costos de las conexiones.

        Returns:
            None

        Raises:
            ValueError: Si no se encuentra la capital en el grafo.
        """
        vertex = self.get_vertex(capital)
        if vertex is None:
            raise ValueError(f"Capital '{capital}' not found in graph.")

        vertex.connections = connections
        vertex.cost = costs
    

    def bfs(self, start: str) -> List[Capital_Node]:
        """
        Método que realiza un recorrido en anchura (BFS) en el grafo.

        Args:
        - start: str que indica la capital de la ciudad de origen.

        Returns:
        - Una lista de objetos Capital_Node que representa el recorrido BFS.
        """
        start_node = self.get_vertex(start)
        if start_node is None:
            return []

        visited_nodes = set()
        bfs_queue = [start_node]
        bfs_path = []

        print("BFS Traversal:")
        while bfs_queue:
            current_node = bfs_queue.pop(0)
            if current_node not in visited_nodes:
                visited_nodes.add(current_node)
                bfs_path.append(current_node)
                print(f"{len(bfs_path)}. {current_node.capital}")
                bfs_queue.extend(neighbor for neighbor in current_node.connections if neighbor not in visited_nodes)

        return bfs_path


    def dfs(self, start: str) -> List[Capital_Node]:
        """
        Método que realiza un recorrido en profundidad (DFS) en el grafo.

        Args:
        - start: str que indica la capital de la ciudad de origen.

        Returns:
        - Una lista de objetos Capital_Node que representa el recorrido DFS.
        """
        start_node = self.get_vertex(start)
        if start_node is None:
            return []

        visited_nodes = set()
        dfs_stack = [start_node]
        dfs_path = []

        print("DFS Traversal:")
        while dfs_stack:
            current_node = dfs_stack.pop()
            if current_node not in visited_nodes:
                visited_nodes.add(current_node)
                dfs_path.append(current_node)
                print(f"{len(dfs_path)}. {current_node.capital}")
                dfs_stack.extend(neighbor for neighbor in current_node.connections if neighbor not in visited_nodes)

        return dfs_path


    def __str__(self):
        """
        Devuelve una representación en cadena del grafo.

        Returns:
            str: La representación en cadena del grafo.
        """
        res = ""
        for vertex in self.vertex_list:
            res += f"\nCapital origen:\n{vertex.capital} (Lat: {vertex.lat}, Long: {vertex.long})\n"
            res += f"Capitales destino:\n"
            printed_connections = set()
            for i, connection in enumerate(vertex.connections):
                if connection.capital not in printed_connections:
                    res += f"\t{connection.capital}, costo: {vertex.cost[i]} km\n"
                    printed_connections.add(connection.capital)
        return res