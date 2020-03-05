import pyodbc


class DBClass:  # DBclass that all classes inherit from, to give them the functions to connect with the DB
    def __init__(self):
        self.conn = self.connect_db()

    @staticmethod
    def connect_db():  # Handles the connection to the DB
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-TBKK5A8K;'
                              'Database=SQL Intro;'
                              'Trusted_Connection=yes;')

        return conn

    def terminal(self, query, show=False):  # method with overloading, true is used with db select statements
        cursor = self.conn.cursor()
        cursor.execute(query)
        list_result = list()
        if show is True:
            for row in cursor:
                list_result.append(row)
            return list_result
        else:
            cursor.commit()

    def extract_store(self):  # Shows the data in a given DB
        #  This should be moved to DBclass and made available to all 3 databases, FUTURE PROJECT
        try:
            database = None
            if self.__class__.__name__ == 'Location':
                database = 'dbo.Location'
            elif self.__class__.__name__ == 'StockItem':
                database = 'dbo.Stockitem'
            elif self.__class__.__name__ == 'Article':
                database = 'dbo.Article'
            else:
                database = __class__.__name__
            query = 'SELECT * from {0}'.format(database)
            return self.terminal(query, show=True)  # uses the terminal overload, since its a select statement
        except:
            return False


class Article(DBClass):  # inherit from DB class, will contain all the functions for Article DB handling
    def __init__(self, article_id, name, description):
        super().__init__()
        self.article_id = article_id
        self.name = name
        self.description = description

    def new_item(self):  # will use the 3 variables to create a new item in Article  DB
        try:
            query = """
            INSERT INTO Article ([Article_Id], [Name], [Description])
            VALUES ('{0}', '{1}', '{2}');
            """.format(self.article_id, self.name, self.description)
            self.terminal(query)
            return True
        except:
            return False

    def rem_item(self):  # Uses only the article_id variable to remove an Article
        try:
            query = """
            DELETE FROM [Article] WHERE [Article_Id] = {0};
            """.format(self.article_id)
            self.terminal(query)
            return True
        except:
            return False

    def mod_item(self):  # Used if you want to update the name or description of an article
        try:
            query = """
            UPDATE [Article]
            SET [Name] = '{0}', [Description] = '{1}'
            WHERE [Article_Id] = {2};
            """.format(self.name, self.description, self.article_id)
            self.terminal(query)
            return True
        except:
            return False
