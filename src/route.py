from city import City

class Route:
    def __init__(self, origin: City, destination: City):
        self.origin = origin
        self.destination = destination
        self.distance = self.calculate_distance()

    def calculate_distance(self):
        return self.origin.distance_to(self.destination)