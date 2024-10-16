from project import connector 
import colorama

#Handles record display
def ret(rollno):
    k = connector.call(f"Select * from student where rollno = {rollno}")[0]
    rollno,name,clas,marks = k[0],k[1],k[2],k[3]
    s = f"""
                      Report on Roll Number {rollno} :- 
      Name >> {name}
      Class >> {clas}
      Marks >> {marks}/100
"""
    return s
