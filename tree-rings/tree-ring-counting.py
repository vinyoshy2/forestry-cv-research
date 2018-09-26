# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
closed = []
edgelist = []
contourlist = []
imgs = []
ruler = cv2.imread("tree-crops/ruler.jpg")
ruler = cv2.resize(ruler,(1360, 15), interpolation = cv2.INTER_CUBIC)
for i in range(1,9):
    img = cv2.imread("tree-crops/" + str(i) + ".jpg")
    imgs.append(img)
    edges = cv2.Canny(img,100,125)
    edgelist.append(edges)
    cv2.imwrite("tree-crops/edges/" + str(i) + ".jpg", edges)
    cimg = img.copy()
    image, contours, hierarchy= cv2.findContours(edges.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contoured = cv2.drawContours(cimg, contours, -1, (0,255,0), 3)
    contourlist.append(contoured)
    cv2.imwrite("tree-crops/contours/" + str(i) + ".jpg", contoured)
    kernel = np.ones((5,1),np.uint8)
    #dilation = cv2.dilate(contoured, kernel,iterations = 1)
    #cv2.imwrite('tree-dilation2.jpg', dilation)
    
    close = cv2.morphologyEx(contoured, cv2.MORPH_CLOSE, kernel)
    closed.append(close)
    cv2.imwrite("tree-crops/closures/" + str(i) + ".jpg", close)



resized_closed = [cv2.resize(closure,(1360, 15), interpolation = cv2.INTER_CUBIC) for closure in closed]
resized_closed.append(ruler)
stacked_closed = np.vstack(tuple(resized_closed))
cv2.imwrite("tree-crops/closures/combined.jpg", stacked_closed)

resized_imgs = [cv2.resize(img,(1360, 15), interpolation = cv2.INTER_CUBIC) for img in imgs]
resized_imgs.append(ruler)
stacked_imgs = np.vstack(tuple(resized_imgs))
cv2.imwrite("tree-crops/combined.jpg", stacked_imgs)

resized_contours = [cv2.resize(contour,(1360, 15), interpolation = cv2.INTER_AREA) for contour in contourlist]
resized_contours.append(ruler)
stacked_contours = np.vstack(tuple(resized_contours))
cv2.imwrite("tree-crops/contours/combined.jpg", stacked_contours)

# Slides a window of width scanRange across image. If intensity of pixel is larger than
# the intensityThreshold, it contributes 1 vote to that window. If pixels in range
# contribute enough votes, it is determined there must be a ring there.
def vote_ring_count(src, scanRange, minimumRingDistance, intensityThreshold, voteThreshold):
    cpy = src.copy()
    height,width,depth = src.shape
    window_left = 0
    window_right = scanRange
    numLines = 0
    while window_right <= width:
        numYes = 0
        for i in range(0, height):
            for j in range(window_left, window_right):    
                vote = src[i,j, 1]
                numYes += (vote >= intensityThreshold)
        if numYes >= (voteThreshold*scanRange*height):
            numLines+=1
            for i in range(0, height):
                cpy[i,window_left+(scanRange + 1) //2, 0] = 0
                cpy[i,window_left+ (scanRange + 1) //2, 1] = 0
                cpy[i,window_left+(scanRange + 1)//2, 2] = 255
            window_left += minimumRingDistance
            window_right += minimumRingDistance
        else:
            window_left += 1
            window_right += 1
    return numLines, cpy

numLines, pic = vote_ring_count(stacked_contours, 1, 10, 255, .4)
print(numLines)
cv2.imwrite("test-votes.jpg", pic)
#Vote Threshold Plots
#lineslist = []
#for i in range(1, 1351):
 #   numLines, pic = vote_ring_count(stacked_contours, 10, 30, 200, i)
  #  lineslist.append(numLines)
#plt.plot(lineslist)
#plt.xlabel("Vote Threshold")
#plt.ylabel("Detected Rings")
#plt.savefig("vote-threshold-plot.jpg")
#plt.show()
    






