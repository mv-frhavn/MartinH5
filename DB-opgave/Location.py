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

        except:
            return False

    def rem_item(self):  # Removes an item from the DB
        try:
            query = """
            DELETE FROM [Location] WHERE [Location_Id] = {0};
            """.format(self.location_id)
            self.terminal(query)

        except:
            return False

    def extract_store(self):  # Shows the data in a given DB
        #  This should be moved to DBclass and made available to all 3 databases, FUTURE PROJECT
        try:
            query = 'SELECT * FROM dbo.Article'
            self.terminal(query, show=True)  # uses the terminal overload, since its a select statement
        except:
            return False
