from project import connector
import colorama


    
#EVALUATES MARKS
def reader(roll_no):
   mark = []
   k = []
   for x in range(0,10):
      a = connector.call(f"Select answer,marks from akey where (QID = {x+1})")[0][0]
      #print(a)
      k.append(a)
   j = []
   #print(k)
   
   for x in range(0,10):        
    f = connector.call(f"Select op{x+1} from answers where (rollno = {roll_no})")[0][0]
    j.append(f)

   for i in range(0,10):
     #print(j[i],k[i])
     if j[i] == k[i]:
       mark.append(10)
     else:
       pass
   
   return(sum(mark))
        

