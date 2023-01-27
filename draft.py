class Location:
    def __init__(self, lat, long):
        self.latitude = lat
        self.longitude = long

    def __str__(self):
        return f"(This is the latitude: {self.latitude}, this is the longitude: {self.longitude})"

    def __repr__(self):
        return f"Location=(Latitude:{self.latitude}, Longitude:{self.longitude})"



bham_academy = Location(52.488, -1.887)
# print(bham_academy)
print(repr(bham_academy))