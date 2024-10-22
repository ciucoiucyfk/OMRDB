patsh = "C:/Users/Abhinav/Documents/Class 12 Project Computer/images"
import cv2,os
import numpy as np
from os import path
import time
from cv import display



def reader(rl):
    f = os.listdir(patsh)
    c=1
    print("\n\n\n")
    for x in f:
        print(f">>> {c}. {x}")
        c+=1
    
    a = input("\n\n Please Enter File Name. ")    
    if a in (f):
        print("Reading file")
        time.sleep(1)
        cvs(a,rl)
    else:
        print("File doesnt Exist")
        input()


def cvs(fi,rl,show = False):
    height = 600
    width = 600

    #PREPROCESSING
    img = cv2.imread(f"{patsh}/{fi}")
    img = cv2.resize(img,(width,height))
    imc = img.copy()
    imgg =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imblur = cv2.GaussianBlur(imgg,(5,5),1)
    imgcan = cv2.Canny(imblur,10,50)

    c,h = cv2.findContours(imgcan,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #CONTOUR MAPPING TO FIND EDGES OF RECTANGLE
    def con(c):
     ret = []
     ars = []
     for x in c:
        ar = cv2.contourArea(x)        
        ars.append(ar)
        if ar > 1000:
            peri = (cv2.arcLength(x,True))
            approx = cv2.approxPolyDP(x,0.01*peri,True)
            if len(approx) == 4:
                ret.append(approx)
     
     return ret

    f = con(c)[0]
       
    #RESIZE PARAMETERS
    def re(p):
        p = p.reshape((4,2))
        pn = np.zeros((4,1,2),np.int32)
        sum = p.sum(1)
        diff = np.diff(p,axis = 1)
        pn[0] = p[np.argmin(sum)] #(0,0)
        pn[3] = p[np.argmax(sum)] #(w,h)
        pn[1] = p[np.argmin(diff)] #(w,0)
        pn[2] = p[np.argmax(diff)]  #(0,h)
        return pn


    #Transforms the image to give a birds eye view 
    if f.size != 0:
        cv2.drawContours(imc,f,-1,(0,0,255),10)    
        b = re(f)
        pt1 = np.float32(b)
        pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pt1,pt2)
        imwarp = cv2.warpPerspective(imc,matrix,(width,height))

    imwg = cv2.cvtColor(imwarp,cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(imwg,120,235,cv2.THRESH_BINARY_INV)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)


    #Slices Transformed image into individual option images and assigns values
    def sp(im):
        box = []
        rows = np.vsplit(im,10)
        c = 1
        for x in rows:          
            col = np.hsplit(x,5)
            for x in col:
                box.append(x)
        return box
    
    v = sp(thresh)

    
    #Showing processed images
    if input("Do you want to view image (y/n) ").lower() == 'y':
        display.imdis((imgg,imblur,imgcan,imwg,thresh,morph),3,250,250)



    #Evaluates The Recieved answer boxes
    def eval(v):
        c = 1
        z = []
        for x in v:
            if cv2.countNonZero(x) > 1850:
                fg = c
                r = True
                while r:
                    if fg-5>0:
                        fg = fg-5
                    else:
                        z.append(fg)
                        r = False
            c+=1
        return z
    vim = (eval(v))

    




    #Associates recieved number stream to alphabetical options
    def counts(li):
        f = []
        holder = ['a','b','c','d','e']
        #print(li)
        for j in range(0,len(li)):
            s = j+1
            o = holder[int(li[j])-1]
            f.append((s,o))
        return f

    s = counts(vim)
    
    print("Completed Reading File")
    print("\n\n\n\n\n\n")

    
    from cv import cvwrite
    cvwrite.write(s,rl)



