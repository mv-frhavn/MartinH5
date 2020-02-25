class Location:
    def __init__(self, location_id, country, city, address):
        self.location_id = location_id
        self.country = country
        self.city = city
        self.address = address


class NewLocation(Location):
    pass


class RemoveLocation(Location):
    pass


