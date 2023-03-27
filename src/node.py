class Node:
    def __init__(self, capital: str) -> None:
        self.capital = capital
        self.connections = []
        self.cost = []
        self.pos = 0
        self.lat = 0
        self.lng = 0

    def __repr__(self) -> str:
        return self.capital