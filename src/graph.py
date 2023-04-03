from node import Capital_Node
import heapq

class Graph:
    """
    Clase que representa un grafo dirigido ponderado. Utiliza la implementación del algoritmo de Floyd-Warshall para
    encontrar los caminos más cortos entre nodos.
    """


    def __init__(self):
        """
        Inicializa un nuevo grafo vacío.
        """
        self.vertex_list: list[Capital_Node] = []  # Lista de nodos del grafo
        self.country_list: list[str] = []  # Lista de nombres de los países correspondientes a cada nodo
        self.dis_matrix = []  # Matriz de distancias entre nodos
        self.pat_matrix = []  # Matriz de recorridos entre nodos


    def distance_matrix(self):
        """
        Crea la matriz de distancias entre nodos.

        Returns:
            La matriz de distancias entre nodos.
        """
        length = len(self.vertex_list)
        matrix = [[float('inf')] * length for _ in range(length)]

        for i in range(length):
            matrix[i][i] = 0

        for vertex in self.vertex_list:
            for idx, connection in enumerate(vertex.connections):
                matrix[vertex.pos][connection.pos] = vertex.cost[idx]

        return matrix


    def path_matrix(self):
        """
        Crea la matriz de recorridos entre nodos.

        Returns:
            La matriz de recorridos entre nodos.
        """
        length = len(self.vertex_list)
        matrix = [[0] * length for _ in range(length)]

        for vertex in self.vertex_list:
            for i in range(length):
                matrix[i][vertex.pos] = vertex

        return matrix


    def Prim(self, start: str):
        """
        Encuentra el árbol de expansión mínimo usando el algoritmo de Prim.

        Args:
            start: El nombre del país del nodo inicial.
        """
        visited = set()
        start_node = self.vertex_list[self.country_list.index(start)]
        edges = [(0, start_node, None)]

        while edges:
            cost, current_node, prev_node = heapq.heappop(edges)

            if current_node not in visited:
                visited.add(current_node)
                if prev_node:
                    # Aquí se puede guardar información sobre la conexión en el árbol de expansión mínimo
                    # Por ejemplo, podría agregar la conexión a una lista de conexiones en el árbol de expansión mínimo
                    pass

                for idx, connection in enumerate(current_node.connections):
                    if connection not in visited:
                        heapq.heappush(edges, (current_node.cost[idx], connection, current_node))


    def short_path_list(self, start: str, end: str):
        """
        Encuentra el camino más corto entre dos nodos.

        Args:
            start: El nombre del país del nodo de inicio.
            end: El nombre del país del nodo de destino.

        Returns:
            La lista de nodos que forman el camino más corto entre el nodo de inicio y el nodo de destino.
        """
        start_node = self.vertex_list[self.country_list.index(start)]
        end_node = self.vertex_list[self.country_list.index(end)]
        path_list = [start_node]
        if end_node in start_node.connections and self.pat_matrix[start_node.pos][end_node.pos] == end_node:
            path_list.append(end_node)
        else:
            aux = end_node
            path = []
            while aux not in start_node.connections:
                aux = self.pat_matrix[start_node.pos][aux.pos]
                path.append(aux)
            path.reverse()
            for node in path:
                path_list.append(node)
            path_list.append(end_node)

        return path_list


    def __str__(self):
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