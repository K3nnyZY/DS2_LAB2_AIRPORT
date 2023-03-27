from node import Node

class Graph:
    def __init__(self) -> None:
        # Cada elemento de la lista de vertices corresponde en su index a la de ciudades
        self.vertex_list:list[Node] = []
        self.capitals_list:list[str] = []
        self.distance_matrix: list[list[int]]
        self.path_matrix: list[list[Node]]

    def MatrizDistancia(self) -> list[list[int]]:
        """Crea la matriz de distancia inicial (Si existe arista el peso, si no infinito)"""
        Matriz = []
        length = len(self.vertex_list)
        for i in range(length):
            Fila = []
            for _ in range(length):
                Fila.append(float("inf"))
            Matriz.append(Fila)
        for i in range(length):
            Matriz[i][i] = 0
        for vertice in self.vertex_list:
            for conexion in vertice.connections:
                Matriz[vertice.pos][conexion.pos] = vertice.cost[vertice.connections.index(conexion)]
        return Matriz