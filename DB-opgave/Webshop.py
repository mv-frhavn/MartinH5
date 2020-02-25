import pyodbc


class Article:
    def __init__(self, name, description, article_id):
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

    def new_art(self):
        try:
            query = """
            INSERT INTO Article ([Article_Id], [Name], [Description])
            VALUES ('{0}', '{1}', '{2}');
            """.format(self.article_id, self.name, self.description)
            self.execute(query)
        except:
            return False

    def rem_art(self):
        try:
            query = """
            DELETE FROM [Article] WHERE [Article_Id] = 3 or [Name] = 'test1';
            """
            cursor = self.conn.cursor()
            cursor.execute(query)
            cursor.commit()

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
            sql = """
            INSERT INTO [Stockitem] ([Stockitem_Id], [ItemNumber], [Weight], [Quantity], [Article_Id], [Location_Id])
            VALUES ('3', '90LM04G0-B01370', '5.6 kg', '1', '3', '3');
            """
            cursor = self.conn.cursor()
            cursor.execute(sql)

            cursor.commit()

        except:
            return False

        #for row in cursor:
         #   print(row)

    def rem_item(self):
        pass

    def inc_quant(self):
        pass

    def dec_quant(self):
        pass


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


item1 = Article('test1', 'total bedst i test', 4).new_art()
