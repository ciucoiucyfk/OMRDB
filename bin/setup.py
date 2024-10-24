#Configuration program
import mysql.connector,pickle
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abhi1234",  
    database = 'meraxes'
    )
cursor = mydb.cursor()
def setup(ini = 0,mod = 0):   
    l = True

    if l == True:
      if ini == 1:
        answer_key()
        credentials()
        student()
        answers()
        if mod == 1:
            install()

def answer_key():
    print("Setting up preloaded answer key ... \n")
    cursor.execute("Create Table akey (QID INT PRIMARY KEY,question VARCHAR(45),answer VARCHAR(45) , marks INT)")    
    mydb.commit()
   
    file= open('C:/Users/Abhinav/Documents/Class 12 Project Computer/bin/config.dat','rb')
    k = pickle.load(file)[0]
    file.close()
    for x in range(1,11):
        cursor.execute(f"insert into akey (QID,answer,marks) values ({x},'{k[x-1]}',10)")
    mydb.commit()
    print("Done \n\n")
    input()


def credentials():
    print("Setting up credentials table.. \n")
    cursor.execute("Create table credentials (usertag varchar(45) primary key , password varchar(45) , ranks varchar(45) )")
    mydb.commit()
    file= open('C:/Users/Abhinav/Documents/Class 12 Project Computer/bin/config.dat','rb')
    k = pickle.load(file)[1]
    file.close()
    cursor.execute(f"insert into credentials (usertag,password,ranks) values ('{k[0]}','{k[1]}','{k[2]}')")
    cursor.execute(f"insert into credentials (usertag,password,ranks) values ('student','a123','studet')")
    mydb.commit()
    print("Done \n\n")
    input()

def answers():
    print("Setting up answers table \n")
    cursor.execute("Create table answers (rollno int primary key)")
    size = 40
    for x in range(0,size):
        cursor.execute(f"alter table answers add column (op{x+1} varchar(10))")
        mydb.commit()
    print("Done \n\n")
    input()

def student():
    print("Setting up student table \n")
    cursor.execute("Create table student (rollno int primary key , name varchar(45) , class int , marks int )")
    mydb.commit()
    print("Done \n\n")
    input() 

def install():
    print("\n\n Setting up modules \n\n\n")
    packages = ["keyboard",'opencv-python','colorama','mysql-connector-python']
    import pip 
    for x in packages:
        print(f'\n\n\nNOW INSTALLING > {x} \n\n\n\n\n\n\n\n\n\n\n')
        pip.main(['install', x])

setup(1,1)
#()
print("YOU CAN BEGIN USING ")
input()
