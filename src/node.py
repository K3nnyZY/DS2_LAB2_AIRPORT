class Capital_Node:
    """
    Clase que representa un nodo en un grafo. Cada nodo corresponde a una capital y está conectado a otros nodos
    mediante arcos con un costo asociado.
    """

    def __init__(self, capital: str) -> None:
        """
        Inicia un nuevo nodo para la capital dada.

        Args:
            capital: El nombre de la capital que representa el nodo.
        """
        self.capital = capital  # Nombre de la capital correspondiente al nodo
        self.connections: list[Capital_Node] = []  # Lista de nodos adyacentes
        self.cost: list[float] = []  # Lista de costos de cada arco que conecta este nodo con sus adyacentes
        self.pos = 0  # Posición del nodo en la lista de nodos del grafo
        self.lat: float = 0  # Latitud geográfica de la capital
        self.long: float = 0  # Longitud geográfica de la capital

    def __repr__(self) -> str:
        """
        Retorna el nombre de la capital que representa el nodo.

        Returns:
            El nombre de la capital que representa el nodo.
        """
        return self.capital
