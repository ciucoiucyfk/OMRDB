from project import connector
import colorama


#### ACCESS CONTROLS

def access(user,passwd):        
        x = connector.call(f"SELECT password FROM credentials WHERE usertag = '{user}' ")        
        #print(x)
        try :
         v = x[0]
        except:
             return ("NO USER")
        else:
             if passwd != v[0]:
                  return "False"
             else :
                  return "PASS"
