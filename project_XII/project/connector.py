import mysql.connector
import colorama


# CENTRAL CONNECTOR FOR PROGRAM


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abhi1234",  
  database = "meraxes"
)
def call(command):
        k = mydb.cursor()
        #print("Fetched")
        k.execute(command)
        return(k.fetchall())
def action(command):
        k = mydb.cursor()
        k.execute(command)
        mydb.commit()
def commit():
        mydb.commit()
def scol(table):
        k= mydb.cursor()
        k.execute(f"describe {table}")
        s = k.fetchall()        
        return(len(s))