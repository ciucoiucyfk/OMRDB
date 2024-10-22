import mysql.connector
from project import connector
import random
from project import reader
from project import eval
import colorama


#HANDLES STUDENT TABLE



def insert():
    name = input("Enter Name ")
    grade = input("Enter Grade ")

    if len(name) == 0:
        print(colorama.Fore.RED,"Please Enter Name")
        input()
        exit()
    else:
     roll_no = random.randint(0,1000000)
     f = connector.call(f"SELECT * FROM student WHERE rollno = '{int(roll_no)}'")    
     if f == []:        
        x = reader.run(roll_no)
        connector.commit()
        connector.commit()
        f  = connector.call(f"Select * From answers where rollno = {roll_no}")[0] 
        vermax = []
        for x in range(0,len(f)):
           if type(f[x])== int:
                pass
           elif f[x] == None:
              #print('d')
              pass
           else:
                vermax.append((x,f[x]))

        print(f"\n\n\n\nUSER ANSWERS >> {vermax}")
        k = eval.reader(roll_no)
        f = connector.action(f"insert into student (rollno,name,class,marks) values ({roll_no},'{name}',{grade},{k})")
        connector.commit()
        
        print(f"\n\n\n\n\n\n     INSERTED NEW ENTRY ROLLNO >> {roll_no}")
        print(f"""

                STATISTICS  :- 
    a) Name :- {name}
    b) Roll No {roll_no}
    c) Grade :- {grade}
    d) Marks :- {k}
    e) Correct :- {k/10}
""")
        
