import pyodbc


class Article:
    def __init__(self, article_id, name, description):
        self.article_id = article_id
        self.name = name
        self.description = description
        self.conn = self.connectdb()

    def connectdb(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-TBKK5A8K;'
                              'Database=SQL Intro;'
                              'Trusted_Connection=yes;')
        return conn

    def execute(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        cursor.commit()
        return

    def new_item(self):
        try:
            query = """
            INSERT INTO Article ([Article_Id], [Name], [Description])
            VALUES ('{0}', '{1}', '{2}');
            """.format(self.article_id, self.name, self.description)
            self.execute(query)
        except:
            return False

    def rem_item(self):
        try:
            query = """
            DELETE FROM [Article] WHERE [Article_Id] = {0};
            """.format(self.article_id)
            self.execute(query)

        except:
            return False

    def mod_item(self):
        try:
            query = """
            UPDATE [Article]
            SET [Name] = '{0}', [Description] = '{1}'
            WHERE [Article_Id] = {2};
            """.format(self.name, self.description, self.article_id)
            self.execute(query)

        except:
            return False


class StockItem(Article):
    def __init__(self, article_id, name, description, stock_item_id, quantity, location_id):
        super().__init__(article_id, name, description)
        self.stock_item_id = stock_item_id
        self.quantity = quantity
        self.location_id = location_id

    def new_item(self):
        try:
            query = """
            INSERT INTO [Stockitem] ([Stockitem_Id], [Quantity], [Article_Id], [Location_Id])
            VALUES ('{0}', '{1}', '{2}', '{3}');
            """.format(self.stock_item_id, self.quantity, self.article_id, self.location_id)
            self.execute(query)

        except:
            return False

    def rem_item(self):
        try:
            query = """
            DELETE FROM [Stockitem] WHERE [Stockitem_Id] = {0};
            """.format(self.stock_item_id)
            self.execute(query)

        except:
            return False

    def mod_quant(self):
        try:
            query = """
            UPDATE [Stockitem]
            SET [Quantity] = '{0}'
            WHERE [Stockitem_Id] = {1};
            """.format(self.quantity, self.stock_item_id)
            self.execute(query)

        except:
            return False

class Location:
    def __init__(self, location_id, position):
        self.location_id = location_id
        self.position = position

    def new_location(self):
        pass

    def rem_location(self):
        pass

    def extract_store(self):
        pass


#item1 = Article('3', 'Razer', 'Naga - mouse with 16 bottoms, decent for MMORPG').mod_art()

#item2 = StockItem('3', 'Razer', 'Naga  Mus', 3, 5, 3).new_item()

