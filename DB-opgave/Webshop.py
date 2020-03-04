import pyodbc


class DBClass:
    def __init__(self):
        self.conn = self.connect_db()

    @staticmethod
    def connect_db():
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-TBKK5A8K;'
                              'Database=SQL Intro;'
                              'Trusted_Connection=yes;')

        return conn

    def terminal(self, query, show=False):
        cursor = self.conn.cursor()
        cursor.execute(query)
        if show is True:
            for row in cursor:
                print(row)
        else:
            cursor.commit()


class Article(DBClass):
    def __init__(self, article_id, name, description):
        super().__init__()
        self.article_id = article_id
        self.name = name
        self.description = description

    def new_item(self):
        try:
            query = """
            INSERT INTO Article ([Article_Id], [Name], [Description])
            VALUES ('{0}', '{1}', '{2}');
            """.format(self.article_id, self.name, self.description)
            self.terminal(query)
        except:
            return False

    def rem_item(self):
        try:
            query = """
            DELETE FROM [Article] WHERE [Article_Id] = {0};
            """.format(self.article_id)
            self.terminal(query)

        except:
            return False

    def mod_item(self):
        try:
            query = """
            UPDATE [Article]
            SET [Name] = '{0}', [Description] = '{1}'
            WHERE [Article_Id] = {2};
            """.format(self.name, self.description, self.article_id)
            self.terminal(query)

        except:
            return False


class StockItem(Article):
    def __init__(self, article_id, name, description, stock_item_id, quantity, location):
        super().__init__(article_id, name, description)
        self.stock_item_id = stock_item_id
        self.quantity = quantity
        self.location = location

    def new_item(self):
        try:
            query = """
            INSERT INTO [Stockitem] ([Stockitem_Id], [Quantity], [Article_Id], [Location_Id])
            VALUES ('{0}', '{1}', '{2}', '{3}');
            """.format(self.stock_item_id, self.quantity, self.article_id, self.location.location_id)
            self.terminal(query)

        except:
            return False

    def rem_item(self):
        try:
            query = """
            DELETE FROM [Stockitem] WHERE [Stockitem_Id] = {0};
            """.format(self.stock_item_id)
            self.terminal(query)

        except:
            return False

    def inc_quant(self):
        try:
            query = """
            update [Stockitem] 
            set Quantity = Quantity + 1 
            where [Stockitem_Id] = {0}
            """.format(self.stock_item_id)
            self.terminal(query)

        except:
            return False

    def dec_quant(self):
        try:
            query = """
            update [Stockitem] 
            set Quantity = Quantity - 1 
            where [Stockitem_Id] = {0}
            """.format(self.stock_item_id)
            self.terminal(query)

        except:
            return False


class Location(DBClass):
    def __init__(self, location_id, position):
        super().__init__()
        self.location_id = location_id
        self.position = position

    def new_item(self):
        try:
            query = """
            INSERT INTO [Location] ([Location_Id], [Position])
            VALUES ({0}, {1});
            """.format(self.location_id, self.position)
            #self.connectdb()
            self.terminal(query)

        except:
            return False

    def rem_item(self):
        try:
            query = """
            DELETE FROM [Location] WHERE [Location_Id] = {0};
            """.format(self.location_id)
            self.terminal(query)

        except:
            return False

    def extract_store(self):
        try:
            query = 'SELECT * FROM dbo.Article'
            self.terminal(query, show=True)
        except:
            return False


item3 = StockItem(4, 'dav', 'God dav do', 4, 4, Location(4, 4)).new_item()

