import cv2
import numpy as np
width = 600
height = 600

img = cv2.imread("sample8.png")
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

f= (con(c)[0])

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
if f.size != 0:
    cv2.drawContours(imc,f,-1,(0,0,255),10)    
    b = re(f)
    pt1 = np.float32(b)
    pt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(pt1,pt2)
    imwarp = cv2.warpPerspective(imc,matrix,(width,height))

imwg = cv2.cvtColor(imwarp,cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(imwg,120,300,cv2.THRESH_BINARY_INV)[1]

def sp(im):
    box = []
    rows = np.vsplit(im,10)
    c = 1
    for x in rows:
        #cv2.imshow(str(c),x)
        #cv2.waitKey(0)        
        #c+=1
        col = np.hsplit(x,5)
        for x in col:
            box.append(x)
    return box
v = sp(thresh)

def eval():
  c = 1
  z = []
  for x in v:
    if cv2.countNonZero(x) > 1000:
        #cv2.imshow(str(c),x)
        #cv2.waitKey(0)    
        #print(cv2.countNonZero(x),c)
        
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
rc = eval()

def counts(li):
    f = []
    holder = ['a','b','c','d','e']
    #print(li)
    for j in range(0,len(li)):
        s = j+1
        o = holder[int(li[j])-1]
        f.append((s,o))
    return f

s = counts(rc)
for x in s:
    print(f"Q.{x[0]} --> {x[1]}")



   



#cv2.imshow('c',thresh)
#cv2.waitKey(0)

