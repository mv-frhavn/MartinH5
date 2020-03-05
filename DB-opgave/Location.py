from Article import DBClass


class Location(DBClass):  # Only inherit from the DB Class
    def __init__(self, location_id, position):
        super().__init__()
        self.location_id = location_id
        self.position = position

    def new_item(self):  # Creates new item in the Location DB
        try:
            query = """
            INSERT INTO [Location] ([Location_Id], [Position])
            VALUES ({0}, {1});
            """.format(self.location_id, self.position)
            self.terminal(query)
            return True
        except:
            return False

    def rem_item(self):  # Removes an item from the DB
        try:
            query = """
            DELETE FROM [Location] WHERE [Location_Id] = {0};
            """.format(self.location_id)
            self.terminal(query)
            return True
        except:
            return False
