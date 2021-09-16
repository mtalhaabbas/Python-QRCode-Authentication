import cv2
import numpy as np
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


while(True):
    success, img = cap.read()
    for code in decode(img):
        myData=code.data.decode('utf-8')
        pts = np.array([code.polygon],np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(255,0,255),5)
        pts2=code.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)
