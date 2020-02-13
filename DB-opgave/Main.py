import pyodbc


class Main:
    def __init__(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-TBKK5A8K;'
                              'Database=SQL Intro;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        sql = 'SELECT * FROM dbo.Article'
        cursor.execute(sql)
        cursor.commit()

        for row in cursor:
            print(row)


Main()