# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:55:04 2018

@author: vinay
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
for i in range(1,7):
    img = cv2.imread("tree-crops/square-crops/" + str(i) + ".jpg")
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(img,50,150,apertureSize = 3)
    lines = cv2.HoughLinesP(edges,1,np.pi/180, 40,minLineLength=50,maxLineGap=30)
    xys = []
    for line in lines:
        #a = np.cos(theta)
        #b = np.sin(theta)
        #x0 = a*rho
        #y0 = b*rho
        #x1 = int(x0 + 1000*(-b))
        #y1 = int(y0 + 1000*(a))
        #x2 = int(x0 - 1000*(-b))
        #y2 = int(y0 - 1000*(a))
        x1,y1,x2,y2 = line[0]
        slope = (y2 - y1) / (x2 - x1)
        if x2 != x1 and slope > 1:
            xys.append((x1,y1,x2,y2))
    prev_x1 = -100000000
    prev_x2 = -100000000
    for x1,y1,x2,y2 in sorted(xys, key = lambda x: x[0]):
        if x1 - prev_x1 > 10 or x1 - prev_x1 < -10:
            if x2 - prev_x2 > 10 or x2 - prev_x2 < 10:
                prev_x1 = x1
                prev_x2 = x2
                cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    plt.imshow(img)
    plt.show()
    