import cv2
import numpy as np
import math as m



def imds(img,offset,width,height):

    
    s = []
    idx = -1
    for i in range(0,len(img)):
        if i%int(offset) == 0:
           s.append([])
           idx+=1           
        res = cv2.resize(img[i],(width,height))
        #print(width,height)
        s[idx].append(res)
    #print(s)
    #print(img)
    if len(s[0])== 1:
        img_blank = np.zeros_like(s[0])
    else:
        img_blank = np.zeros_like(s[0][0])
    for w in s:        
        while len(w) != offset:
            w.append(img_blank)
    gh = []
    #print("POITN")
    for l in s:
        r = np.hstack(tuple(l))        
        gh.append(r)
    v = np.vstack(tuple(gh))
    cv2.imshow('Image Display',v)
    #cv2.waitKey(0)
    #c#v2.destroyAllWindows()



