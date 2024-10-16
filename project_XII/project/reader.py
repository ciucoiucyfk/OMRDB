from project import connector
import random
import colorama

# Current placeholder for opencv
def rapid(roll_no):
  x = ['a','b','c','d']
  connector.action(f"insert into answers (rollno) values ({roll_no})")
  for i in range(0,10):
    k = random.randint(0,3)
    connector.action(f'update answers set op{i+1} = "{x[k]}" where (rollno = {roll_no})')

import sys
sys.path.append('cv/')
def run(roll_no):
    from cv import cv
    cv.reader(roll_no)
