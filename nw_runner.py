# establish connection like before
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

# # Create an object that relates only to the Products table
# prod_rows = cursor.execute("SELECT * FROM Products").fetchall()
# print(prod_rows)

# Create a new table
new_table = cursor.execute("CREATE TABLE Isobel (ID INT IDENTITY(1,1) PRIMARY KEY,Name VARCHAR(20), Age INT)")

new_rows = cursor.execute("SELECT * FROM Isobel").fetchall()

print(new_rows)
