# manages admin controls of program
from project import connector
import colorama
import cv2
import numpy as np

def run():
    print("""
    1.Add New User
    2.Alter Answer Key 
    3.Display all marks
    4.Cross Checker
""")
    vermax = ['5.Purge Tables','6.Drop tables (MUST RUN SETUP BEFORE RERUNNING PROGRAM)','7.Exit']
    for la  in vermax:
        print(colorama.Back.RED,colorama.Fore.WHITE,f"  {la.lstrip()}",colorama.Back.RESET,colorama.Fore.RESET,colorama.Fore.GREEN)
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
    
    elif f == 5:
        c = connector.call("select rollno from student")
        d = connector.call("select rollno from answers")
        print("ARE YOU SURE ENTER PASSKEY TO CONFIRM")
        if input("PASSKEY >> ") == 'meraxes':            
        #print("DEBUG START")
        #print(c,d)
         if len(c) == 0:
            if len(d) == 0:
                print(colorama.Fore.BLUE,"<<ADMIN>>  NO SUCH TABLE EXISTS PLEASE EXIT")                
                input()
                exit()
         else:
            for w in c:
                #print(w[0])
                connector.action(f"delete from student where (rollno = {int(w[0])})")
                connector.action(f"delete from answers where (rollno = {int(w[0])})")
                connector.commit()
                import os
                for x in os.listdir('project_XII/holder'):
                    for l in os.listdir(f'project_XII/holder/{x}'):
                        os.remove(f'project_XII/holder/{x}/{l}')
                    os.rmdir(f'project_XII/holder/{x}')
            print(f"<<ADMIN>>  PURGED ALL {len(c)} ENTRIES FROM TABLES STUDENT AND ANSWERS")
        
    elif f == 6:
        print("ARE YOU SURE ENTER PASSKEY TO CONFIRM")
        if input("PASSKEY >> ") == 'meraxes':  
            connector.action("DROP TABLE STUDENT")  
            connector.action("DROP TABLE answers")  
            connector.action("DROP TABLE credentials")  
            connector.action("DROP TABLE akey")  
            print("<<ADMIN>>  DROPPED ASSOCIATED TABLE PLEASE RERUN SETUP")
            input()
            exit()

    elif f == 3:
        c = connector.call("select * from student")
        print('\n\n\n\n\n')
        for y in c:
            print(f"<<ADMIN>> Rollno > {y[0]}  Name >> {y[1]}   Grade >> {y[2]}   Marks >> {y[3]}")
    
    elif f ==2:
        (sjr) = input("Enter size of answer key ");sjr=int(sjr)
        print(f"<<ADMIN>> Enter options without space (MUST BE {sjr} options from a >> e)")
        f = tuple(input(">> "))
        if len(f) != (sjr):
            print(f,len(f),(sjr))            
            print("<<ADMIN>> INVALID ANSWER KEY LOADED REJECTING....")
            input()
            exit()
        else:
            connector.action("DROP TABLE akey")  
            print("Setting up preloaded answer key ... \n")
            connector.action("Create Table akey (QID INT PRIMARY KEY,question VARCHAR(45),answer VARCHAR(45) , marks INT)")    
            connector.commit()
            for x in range(0,(sjr)):
                connector.action(f"insert into akey (QID,answer,marks) values ({x+1},'{f[x]}',10)")
            print("\n\n\n\n<<ADMIN>> CHANGED ANSWER KEY .")
    elif f == 4:        
        s = connector.call("Select rollno,name from student")
        k = len(s)
        i = 1
        for l in s:
            print(f'{i}. {l[1]} >> {l[0]}');i+=1
        f = input(f'Choose roll no ')
        ans = connector.call(f"select * from answers where rollno = {f}")[0]
        p = connector.call(f"Select * from akey");phi = []
        

        import os
        imgal = []
        if input("View Images associated?? ").lower() == 'y':
            for n in os.listdir(f'C:/Users/Abhinav/Documents/Class 12 Project Computer/project_XII/holder/{f}'):
                print(n)
                kla = cv2.imread(f'C:/Users/Abhinav/Documents/Class 12 Project Computer/project_XII/holder/{f}/{n}',0)
                #cv2.imshow('a',kla)
                #cv2.waitKey(0)
                imgal.append(kla)
                
                
            from project import display

            display.imds(tuple(imgal),4,250,180)


            
        for n in p:
            phi.append(n[2])
        i = 1
        for s in range(0,len(phi)):
            if phi[s] == ans[s+1]:                
                print(f'{i}. UA >> {ans[s+1]} | AK >> {phi[s]}      ',end= '')                
                print(colorama.Back.GREEN,colorama.Fore.WHITE,'CORRECT',colorama.Back.RESET,colorama.Fore.RESET,colorama.Fore.GREEN)
            elif ans[s+1] == None:
                print(f'{i}. UA >> {ans[s+1]} | AK >> {phi[s]}      ',end= '')                
                print(colorama.Back.YELLOW,colorama.Fore.WHITE,'NOT ATTEMPTED',colorama.Back.RESET,colorama.Fore.RESET,colorama.Fore.GREEN)
            else:
                print(f'{i}. UA >> {ans[s+1]} | AK >> {phi[s]}      ',end= '')                
                print(colorama.Back.RED,colorama.Fore.WHITE,'INCORRECT',colorama.Back.RESET,colorama.Fore.RESET,colorama.Fore.GREEN)

            i+=1
        #print("LLLLDLD")
        #print(p)
                
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:exit()