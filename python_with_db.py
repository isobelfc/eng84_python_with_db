# To establish connection between Python and SQL we will use PYODBC
import pyodbc

# Let's establish the connection using PYODBC
server = "18.135.103.95"  # ip
database = "Northwind"  # name of DB, case sensitive
username = "SA"
password = "Passw0rd2018"
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)  # validates the connection

# Let's check if the connection has been validated and cursor object is created
cursor = docker_Northwind.cursor()
print(cursor.execute("Select @@version;"))

# Let's fetch some data from the Northwind DB
row = cursor.fetchone()
print(row)

# Let's connect ot our DB and fetch some data from Customers table
cust_rows = cursor.execute("SELECT * FROM Customers").fetchall()
print(cust_rows)
# We use execute to run our queries within a string
# fetchall() gets all the data from the table

prod_rows = cursor.execute("SELECT * FROM Products").fetchall()
# Let's iterate through the Products table and check the UnitPrices available
for records in prod_rows:
    print(records.UnitPrice)

row = cursor.execute("SELECT * FROM Products")
while True:
    record = row.fetchone()
    if record is None:
        break
    print(record.UnitPrice)
