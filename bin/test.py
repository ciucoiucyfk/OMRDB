import mysql.connector
import colorama


# CENTRAL CONNECTOR FOR PROGRAM


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abhi1234",  
  database = "meraxes"
)
c = mydb.cursor()

c.execute("describe akey")
for x in c.fetchall():
    print(x)