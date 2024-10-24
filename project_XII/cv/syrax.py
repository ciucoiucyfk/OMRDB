import cv2
import numpy as np
import os
def coll(ims,tag):    
    path = 'C:/Users/Abhinav/Documents/Class 12 Project Computer/project_XII/holder'    
    f = os.mkdir(f'{path}/{tag}')
    i = 1
    for x in ims:
        cv2.imwrite(f'{path}/{tag}/{i}.jpg',x)
        i+=1
        #cv2.imshow('s',x)
        #cv2.waitKey(0)