import pyodbc

class NwProducts:
    def __init__(self):
        # login details - removed in Github push
        self.server = "XXX"
        self.database = "Northwind"  # name of DB, case sensitive
        self.username = "XXX"
        self.password = "XXX"

        # connect to server
        self.docker_Northwind = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        self.cursor = self.docker_Northwind.cursor()

    # get all data from products table
    def retrieve_all_product_data(self):
        row = self.cursor.execute("SELECT * FROM Products")
        while True:
            record = row.fetchone()
            if record is None:
                break
            print(record.UnitPrice)
