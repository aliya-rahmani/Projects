import cv2 as cv
import numpy as np 

draw = False
erase = False

def draw_circle(event,x,y,flags,param):
    global draw,erase
    if event == cv.EVENT_RBUTTONDOWN:
        erase = True
    if event == cv.EVENT_LBUTTONDOWN:
        draw = True
    elif event == cv.EVENT_MOUSEMOVE:
        if draw == True:
            cv.rectangle(img,(x,y),(x+2,y+2),(0,255,255),-1,cv.LINE_AA)
        elif erase == True:
            cv.rectangle(img,(x,y),(x+5,y+5),(0,0,0),-1,cv.LINE_AA)
    elif event == cv.EVENT_LBUTTONUP:
        draw = False
    elif event == cv.EVENT_RBUTTONUP:
        erase = False
img = np.zeros((512,512,3),np.uint8)
cv.namedWindow('Paint')
cv.setMouseCallback('Paint',draw_circle)

while(1):
    cv.imshow('Paint',img)
    if cv.waitKey(1) & 0xFF == 27:
        break
cv.destroyAllWindows()
