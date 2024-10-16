# manages admin controls of program
from project import connector
import colorama

def run():
    print("""
    1.Add New User
    2.Alter Answer Key 
    3.Purge Tables
    4.Display all marks
    5.Drop tables (MUST RUN SETUP BEFORE RERUNNING PROGRAM)
    6.Exit
""")
    f = int(input("Choose "))
    if f == 1:
        user = ''
        r = 0
        while r == 0:
            user = input("Enter Usertag  ")
            s = connector.call(f"select * from credentials where usertag = '{user}' ")
            #print(s)
            if len(s) == 0:
                user = user
                r = 1
        password = input("Enter password ")
        pass_c = input("Confirm Password ")
        if pass_c == password:
            rank = input("Choose rank ")
            #print(rank)
            connector.action(f"insert into credentials (usertag,password,ranks) values ('{user}','{pass_c}','{rank}')")
            print(colorama.Fore.BLUE,"<<ADMIN>> ADDED USER SUCCESSFULLY ")
            exit()           
        else:
            print(colorama.Fore.BLUE,"<<ADMIN>> Unmatched Password ... EXITING")
            input()
            exit()
    
    elif f == 3:
        c = connector.call("select rollno from student")
        d = connector.call("select rollno from answers")
        if len(c) == 0:
            if len(d) == 0:
                print(colorama.Fore.BLUE,"<<ADMIN>>  NO SUCH TABLE EXISTS PLEASE EXIT")                
                input()
                exit()
        else:
            for w in c:
                connector.action(f"delete from student where (rollno = {w[0]})")
                connector.action(f"delete from answers where (rollno = {w[0]})")
                connector.commit()
            print(f"<<ADMIN>>  PURGED ALL {len(c)} ENTRIES FROM TABLES STUDENT AND ANSWERS")
        
    elif f == 5:
        connector.action("DROP TABLE STUDENT")  
        connector.action("DROP TABLE answers")  
        connector.action("DROP TABLE credentials")  
        connector.action("DROP TABLE akey")  
        print("<<ADMIN>>  DROPPED ASSOCIATED TABLE PLEASE RERUN SETUP")
        input()
        exit()

    elif f == 4:
        c = connector.call("select * from student")
        print('\n\n\n\n\n')
        for y in c:
            print(f"<<ADMIN>> Rollno > {y[0]}  Name >> {y[1]}   Grade >> {y[2]}   Marks >> {y[3]}")
    
    elif f ==2:
        print("<<ADMIN>> Enter options without space (MUST BE 10 options from a >> e)")
        f = tuple(input(">> "))
        if len(f) != 10:
            #print(f,len(f))            
            print("<<ADMIN>> INVALID ANSWER KEY LOADED REJECTING....")
            input()
            exit()
        else:
            connector.action("DROP TABLE akey")  
            print("Setting up preloaded answer key ... \n")
            connector.action("Create Table akey (QID INT PRIMARY KEY,question VARCHAR(45),answer VARCHAR(45) , marks INT)")    
            connector.commit()
            for x in range(1,11):
                connector.action(f"insert into akey (QID,answer,marks) values ({x},'{f[x-1]}',10)")
            print("\n\n\n\n<<ADMIN>> CHANGED ANSWER KEY .")
                


        

    else:exit()