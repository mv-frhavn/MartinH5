import pyodbc
from Webshop import StockItem
#from Webshop import Location
#from Webshop import Article


class Main:




        for row in cursor:
            print(row)

    def sqlquery(self, sql):
        cursor = conn.cursor()
        #sql = 'SELECT * FROM dbo.Article'
        cursor.execute(sql)

        cursor.commit()


Main()

