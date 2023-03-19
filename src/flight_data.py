class FlightData:
    def __init__(self):
        self.capitals = []
        self.routes = []

    def load_capitals(self):
        # Carga información de las capitales y crea objetos City
        pass

    def load_routes(self):
        # Carga información de las rutas de vuelo y crea objetos Route
        pass

    def get_city_by_code(self, code: str):
        for city in self.capitals:
            if city.airport_code == code:
                return city
        return None