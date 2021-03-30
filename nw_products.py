class NwProducts:
    def __init__(self):
        # login details
        self.server = "XXX"
        self.database = "Northwind"  # name of DB, case sensitive
        self.username = "XXX"
        self.password = "XXX"

        # connect to server
        self.docker_Northwind = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

        self.cursor = docker_Northwind.cursor()

        self.cursor.execute("SELECT * INTO Isobel FROM Products")