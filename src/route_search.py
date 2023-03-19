from typing import List
from flight_data import FlightData
import heapq
from city import City
import itertools


class RouteSearch:
    def __init__(self, flight_data: FlightData):
        self.flight_data = flight_data

    def shortest_path(self, origin: str, destination: str):
        origin_city = self.flight_data.get_city_by_code(origin)
        destination_city = self.flight_data.get_city_by_code(destination)

        if origin_city is None or destination_city is None:
            return None

        distances = {city: float('inf') for city in self.flight_data.capitals}
        previous_cities = {city: None for city in self.flight_data.capitals}
        distances[origin_city] = 0
        priority_queue = [(0, origin_city)]

        while priority_queue:
            current_distance, current_city = heapq.heappop(priority_queue)

            if current_distance > distances[current_city]:
                continue

            for route in self.flight_data.routes:
                if route.origin == current_city:
                    neighbor = route.destination
                    new_distance = current_distance + route.distance

                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous_cities[neighbor] = current_city
                        heapq.heappush(priority_queue, (new_distance, neighbor))

        # Reconstruct the shortest path
        path = []
        city = destination_city
        while city is not None:
            path.append(city)
            city = previous_cities[city]
        path.reverse()

        return path if path[0] == origin_city else None
    
    def shortest_paths_to_all(self, origin: str):
        origin_city = self.flight_data.get_city_by_code(origin)

        if origin_city is None:
            return None

        other_cities = [city for city in self.flight_data.capitals if city != origin_city]

        shortest_path = None
        shortest_distance = float('inf')

        for city_permutation in itertools.permutations(other_cities):
            path = [origin_city] + list(city_permutation)
            distance = self.path_distance(path)

            if distance < shortest_distance:
                shortest_distance = distance
                shortest_path = path

        return shortest_path

    def path_distance(self, path: List[City]):
        distance = 0
        for i in range(len(path) - 1):
            city1, city2 = path[i], path[i + 1]
            route = self.find_route(city1, city2)
            if route:
                distance += route.distance
            else:
                return float('inf')  # Return infinite distance if no direct route exists
        return distance

    def find_route(self, origin: City, destination: City):
        for route in self.flight_data.routes:
            if route.origin == origin and route.destination == destination:
                return route
        return None


class FlightRouteApp:
    def __init__(self):
        self.flight_data = FlightData()
        self.route_search = RouteSearch(self.flight_data)

    def find_all_routes(self, origin: str):
        return self.route_search.shortest_paths_to_all(origin)

    def find_route(self, origin: str, destination: str):
        return self.route_search.shortest_path(origin, destination)
