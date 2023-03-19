import math

class City:
    def __init__(self, name: str, country: str, latitude: float, longitude: float, airport_code: str):
        self.name = name
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.airport_code = airport_code

    def distance_to(self, city):
        def haversine(lat1, lon1, lat2, lon2):
            R = 6371  # radio de la Tierra en km
            dlat = math.radians(lat2 - lat1)
            dlon = math.radians(lon2 - lon1)
            lat1, lon1, lat2, lon2 = map(math.radians, (lat1, lon1, lat2, lon2))

            a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
                 math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) * math.sin(dlon / 2))
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            return R * c

        return haversine(self.latitude, self.longitude, city.latitude, city.longitude)
