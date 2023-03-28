from node import Capital_Node


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


    def Floyd_Warshall(self):
        """
        Encuentra los caminos más cortos entre todos los pares de nodos utilizando el algoritmo de Floyd-Warshall.
        """
        # Si la matriz de distancia no ha sido creada, la creamos
        if not self.dis_matrix:
            self.dis_matrix = self.distance_matrix()

        # Si la matriz de recorrido no ha sido creada, la creamos
        if not self.pat_matrix:
            self.pat_matrix = self.path_matrix()

        n = len(self.vertex_list)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    temp = self.dis_matrix[i][k] + self.dis_matrix[k][j]
                    if temp < self.dis_matrix[i][j]:
                        self.dis_matrix[i][j] = temp
                        self.pat_matrix[i][j] = self.vertex_list[k]


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