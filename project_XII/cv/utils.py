import cv2
import numpy as np
width = 600
height = 1000

img = cv2.imread("b5.jpg")
img = cv2.resize(img,(width,height))
imc = img.copy()
imgg =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imblur = cv2.GaussianBlur(imgg,(5,5),1)
imgcan = cv2.Canny(imblur,10,50)

c,heirarchy = cv2.findContours(imgcan,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


def con(c):
    ret = []
    ars = []
    for x in c:
        ar = cv2.contourArea(x)        
        ars.append(ar)
        if ar > 1000:
            peri = (cv2.arcLength(x,True))
            approx = cv2.approxPolyDP(x,0.01*peri,True)

            ##cv2.drawContours(imc,approx,-1,(0,0,255),10)
            #cv2.imshow('c',imc)
            #cv2.waitKey(0)

            if len(approx) == 4:
                ret.append(approx)
    #print(max(ars))
    return ret

wr= (con(c))
try:
    wr[0],wr[1],wr[2],wr[3]= wr[2],wr[3],wr[0],wr[1]
except:
    pass
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

w = 600
h = 600
sc = 0.60
import math
width = math.ceil(w*sc)
height = math.ceil(h*sc)
r = []
print(len(wr))

import time
xs = []
def sp(im):
    r = np.vsplit(im,10)
    for sh in r:
        f = np.hsplit(sh,5)
        for s in f:            
            #cv2.imshow('s',s)
            #cv2.waitKey(0)
            xs.append(s)

for f in wr:
    if f.size != 0:
        cv2.drawContours(imc,f,-1,(0,0,255),10)    
        b = re(f)
        pt1 = np.float32(b)
        pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pt1,pt2)
        imwarp = cv2.warpPerspective(imc,matrix,(width,height))
        imwg = cv2.cvtColor(imwarp,cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(imwg,120,300,cv2.THRESH_BINARY_INV)[1]
        sp(thresh)
        cv2.imshow('s',thresh)
        cv2.waitKey(0)


def eval():
  c = 1
  z = []
  syrax = 1  
  for x in xs:
    if cv2.countNonZero(x) > 1000:
        #cv2.imshow('f',x)
        #cv2.waitKey(0)        
        fg = c
        r = True
        while r:
            if fg-5>0:
                fg = fg-5                
            else:
                z.append([fg,syrax])
                r = False
                #print(syrax)
    c+=1
    if (c-1)%5 == 0:
        syrax+=1
  return z
rc = eval()


def counts(li):
    f = []
    holder = ['a','b','c','d','e']
    #print(li)
    for j in range(0,len(li)):
        s = li[j][1]
        g = True
        for x in f :
            if x[0] == s:
                g = False
        if g == False:
            pass
        else:
            o = holder[int(li[j][0])-1]
            f.append((s,o))
    return f


s = counts(rc)
print(s)