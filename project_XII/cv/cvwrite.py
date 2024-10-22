import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abhi1234",  
  database = "meraxes"
)
c = mydb.cursor()

def write(tu,rl):
    c.execute(f"insert into answers (rollno) values ({rl}) ")
    mydb.commit()
    for x in tu:
        try:
          c.execute(f"update answers set op{x[0]} = '{x[1] }' where (rollno = {rl})")
          mydb.commit()
        except:
           pass
        else:
           pass
    #c.execute(f"select * from answers where rollno = {rl}")
    #print(c.fetchall())
