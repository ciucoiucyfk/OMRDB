# MAIN CONSOLE FOR PROGRAM
from project import access
from project import connector
from project import admin
from project import dbhan
import colorama
import os


level = 1
def main(): 
    username = input("Please enter your assigned username ")
    password = input("Please enter your assigned password ")
    k = access.access(username,password)     
    if k == "PASS":
        if username == 'master': 
            global level 
            level = 2
        else:
            level = 1
        print(colorama.Fore.YELLOW,f"ACCESS GRANTED FOR USER {username}")        
        prog()
    else:
        print(colorama.Fore.RED,"ACCESS DENIED")

def record():
    from project import record
    k = input("Enter your roll no (999 to exit):- ")
    if k == 999:
        exit()
    else:
        print(colorama.Fore.GREEN,record.ret(k))

def prog():
    while True:
        print(colorama.Fore.CYAN,"ENTERED CONSOLE :-")
        print(colorama.Fore.CYAN,"level = ",level)
        if level == 2:
            men = """
    1.Access Records
    2.Read sheet
    3.Access Answer Key
    4.Admin Controls
    5.Clear screen
    6.Exit   
"""     
            print(colorama.Fore.GREEN,men)
            k = int(input("Choose :- "))
            if k == 6:
                exit()                
            elif k ==1:
                record()
            elif k == 2:
                dbhan.insert()
            elif k == 3:
                k = connector.call("select answer from akey");c = 1
                for x in k:                    
                    print(f'Q.{c} > {x[0]}')
                    c+=1
                print('\n\n\n\n')
            elif k == 4:
                admin.run()
            elif k == 5:
                os.system('cls')

        else:
            record()

