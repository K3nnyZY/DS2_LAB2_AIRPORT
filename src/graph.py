from node import Node

class Graph:

    def __init__(self) -> None:
        # Cada elemento de la lista de vertices corresponde en su index a la de ciudades
        self.vertexlist: list[Node] = []
        self.countrylist: list[str] = []
        self.MatrizDis: list[list[int]]
        self.MatrizRec: list[list[Node]]

    def distance_matrix(self) -> list[list[int]]:
        """Crea la matriz de distancia inicial (Si existe arista el peso, si no infinito)"""
        Matriz = []
        length = len(self.vertexlist)

        for i in range(length):
            Fila = []

            for _ in range(length):
                Fila.append(float("inf"))
            Matriz.append(Fila)

        for i in range(length):
            Matriz[i][i] = 0
        for vertex in self.vertexlist:

            for connection in vertex.connections:
                Matriz[vertex.pos][connection.pos] = vertex.cost[vertex.connections.index(connection)]

        return Matriz
    

    def path_matrix(self):
        matrix = []
        length = len(self.vertexlist)

        for i in range(length):
            row = []
            for j in range(length):
                row.append(0)
            matrix.append(row)

            for vertex in self.vertexlist:
                for i in range(length):
                    matrix[i][vertex.pos] = vertex
        return matrix
    

    def floyd_warshall(self):

        n = len(self.vertexlist)
        matrix = self.distance_matrix()
        matrixP = self.path_matrix()

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    Min = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                    if Min != matrix[i][j]:
                        matrixP[i][j] = self.vertexlist[k]
                    matrix[i][j] = Min

        self.MatrizDis = matrix
        self.MatrizRec = matrixP


    def path_list(self, start:str, end:str):

        node_1 = self.vertexlist[self.countrylist.index(start)]
        node_2 = self.vertexlist[self.countrylist.index[end]]

        list = [node_1]

        if node_2 in node_1.connections and self.MatrizRec[node_1.pos][node_2.pos] == node_2:
            pass