import cv2
import numpy as np
from util import *
import os

img = cv2.imread('IMG_4465_zoom.jpg')

cwd = os.getcwd()
#Canny Edge Detection
binary_img = cv2.Canny(img, 100, 110)
cv2.imwrite(cwd+'/canny_edge/IMG_4468_zoom_canny_edge.jpg', binary_img)

px_mm = 1818/float(1400)

#ret,thresh = cv2.threshold(binary_img,127,255,0)
#_, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
_, contours, hierarchy = cv2.findContours(binary_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

#RETR_TREE : retrieves all of the contours and reconstructs a full hierarchy of nested contours.
#CHAIN_APPROX_SIMPLE : compresses horizontal, vertical, and diagonal segments and leaves only their end points.
#For example, an up-right rectangular contour is encoded with 4 points.

print "Original # of Contours:",len(contours) #how many contour lines
#print contours
prunedContours = [contour for contour in contours if len(contour) > 4]
print "Filtering contours for at least 4 points:",len(prunedContours)

#area stats
#area = [cv2.contourArea(contour) for contour in prunedContours if cv2.contourArea(contour) > 0]
height, width = img.shape[:2]
img_covered = np.zeros((height, width))
prunedContours.sort(reverse=True, key=lambda x: xy_area(x))
#------------------------------------------------------------------
area = [xy_area(contour) for contour in prunedContours]
area_np = np.array(area)
area_np = reject_outliers(area_np)
print "Min area:", min(area_np)
print "Max area:", max(area_np)
mean = np.mean(area_np)
print "Mean area:",mean
print "Median area:",np.median(area_np)
std = np.std(area_np)
print "STD:",std
#Buckets
print "10% Bucket:",len([a for a in area_np if a < max(area_np)*0.1])
print "20% Bucket:",len([a for a in area_np if a >= max(area_np)*0.1  and a < max(area_np)*0.2])
print "30% Bucket:",len([a for a in area_np if a >= max(area_np)*0.2  and a < max(area_np)*0.3])
print "40% Bucket:",len([a for a in area_np if a >= max(area_np)*0.3  and a < max(area_np)*0.4])
print "50% Bucket:",len([a for a in area_np if a >= max(area_np)*0.4  and a < max(area_np)*0.5])
print "60% Bucket:",len([a for a in area_np if a >= max(area_np)*0.5  and a < max(area_np)*0.6])
print "70% Bucket:",len([a for a in area_np if a >= max(area_np)*0.6  and a < max(area_np)*0.7])
print "80% Bucket:",len([a for a in area_np if a >= max(area_np)*0.7  and a < max(area_np)*0.8])
print "90% Bucket:",len([a for a in area_np if a >= max(area_np)*0.8  and a < max(area_np)*0.9])
print "100% Bucket:",len([a for a in area_np if a >= max(area_np)*0.9])
#---------------------------------------------------------------------

print "------ADJUSTED------ throw out values greater than 10*median"
area = [xy_area(contour) for contour in prunedContours if xy_area(contour) < 10*np.median(area_np)]
area_np = np.array(area)
area_np = reject_outliers(area_np)
print "Min area:", min(area_np)
print "Max area:", max(area_np)
mean = np.mean(area_np)
print "Mean area:",mean
print "Median area:",np.median(area_np)
std = np.std(area_np)
print "STD:",std
#Buckets
print "10% Bucket:",len([a for a in area_np if a < max(area_np)*0.1])
print "20% Bucket:",len([a for a in area_np if a >= max(area_np)*0.1  and a < max(area_np)*0.2])
print "30% Bucket:",len([a for a in area_np if a >= max(area_np)*0.2  and a < max(area_np)*0.3])
print "40% Bucket:",len([a for a in area_np if a >= max(area_np)*0.3  and a < max(area_np)*0.4])
print "50% Bucket:",len([a for a in area_np if a >= max(area_np)*0.4  and a < max(area_np)*0.5])
print "60% Bucket:",len([a for a in area_np if a >= max(area_np)*0.5  and a < max(area_np)*0.6])
print "70% Bucket:",len([a for a in area_np if a >= max(area_np)*0.6  and a < max(area_np)*0.7])
print "80% Bucket:",len([a for a in area_np if a >= max(area_np)*0.7  and a < max(area_np)*0.8])
print "90% Bucket:",len([a for a in area_np if a >= max(area_np)*0.8  and a < max(area_np)*0.9])
print "100% Bucket:",len([a for a in area_np if a >= max(area_np)*0.9])

#-------------------------------------------------------------------------
print "------polyContoursDP------"
polyContours = [cv2.approxPolyDP(contour, 3, True) for contour in prunedContours]
area = [cv2.contourArea(contour) for contour in polyContours if cv2.contourArea(contour) > 0]
area_np = np.array(area)
area_np = reject_outliers(area_np)
print "Min area:", min(area_np)
print "Max area:", max(area_np)
mean = np.mean(area_np)
print "Mean area:",mean
print "Median area:",np.median(area_np)
std = np.std(area_np)
print "STD:",std
#Buckets
print "10% Bucket:",len([a for a in area_np if a < max(area_np)*0.1])
print "20% Bucket:",len([a for a in area_np if a >= max(area_np)*0.1  and a < max(area_np)*0.2])
print "30% Bucket:",len([a for a in area_np if a >= max(area_np)*0.2  and a < max(area_np)*0.3])
print "40% Bucket:",len([a for a in area_np if a >= max(area_np)*0.3  and a < max(area_np)*0.4])
print "50% Bucket:",len([a for a in area_np if a >= max(area_np)*0.4  and a < max(area_np)*0.5])
print "60% Bucket:",len([a for a in area_np if a >= max(area_np)*0.5  and a < max(area_np)*0.6])
print "70% Bucket:",len([a for a in area_np if a >= max(area_np)*0.6  and a < max(area_np)*0.7])
print "80% Bucket:",len([a for a in area_np if a >= max(area_np)*0.7  and a < max(area_np)*0.8])
print "90% Bucket:",len([a for a in area_np if a >= max(area_np)*0.8  and a < max(area_np)*0.9])
print "100% Bucket:",len([a for a in area_np if a >= max(area_np)*0.9])

polyContours.sort(reverse=True, key=lambda x: cv2.contourArea(x))
polyContours = [contour for contour in polyContours if cv2.contourArea(contour) > 0]
print "Final # of polyContours:", len(polyContours)
#-------------------------------------------------------------------------
print "---------merging contours-----------"
mergedContours = []
alreadyMerged = {}
for i in range(0, len(polyContours)):
    alreadyMerged[i] = []
for i in range(0, len(polyContours)):
    contour1 = polyContours[i]
    for j in range(0, len(polyContours)):
        contour2 = polyContours[j]
        if i != j and (distance(contour1[0], contour2[0]) < 6 or distance(contour1[len(contour1)-1], contour2[0]) < 6
         or distance(contour1[0], contour2[len(contour2)-1]) < 6 or distance(contour1[len(contour1)-1], contour2[len(contour2)-1]) < 6):
            if j not in alreadyMerged[i]:
                mergedContours += [np.concatenate((contour1, contour2))]
                alreadyMerged[i] += [j]
                alreadyMerged[j] += [i]
    if len(alreadyMerged[i]) == 0:
        mergedContours += [contour1]
print "# of mergedContours:", len(mergedContours)

#area = [cv2.contourArea(contour) for contour in mergedContours]
area = [xy_area(contour) for contour in mergedContours]
area_np = np.array(area)
area_np = reject_outliers(area_np)
print "Min area:", min(area_np)
print "Max area:", max(area_np)
mean = np.mean(area_np)
print "Mean area:",mean
median = np.median(area_np)
print "Median area:",median
std = np.std(area_np)
print "STD:",std
#Buckets
print "10% Bucket:",len([a for a in area_np if a < max(area_np)*0.1])
print "20% Bucket:",len([a for a in area_np if a >= max(area_np)*0.1  and a < max(area_np)*0.2])
print "30% Bucket:",len([a for a in area_np if a >= max(area_np)*0.2  and a < max(area_np)*0.3])
print "40% Bucket:",len([a for a in area_np if a >= max(area_np)*0.3  and a < max(area_np)*0.4])
print "50% Bucket:",len([a for a in area_np if a >= max(area_np)*0.4  and a < max(area_np)*0.5])
print "60% Bucket:",len([a for a in area_np if a >= max(area_np)*0.5  and a < max(area_np)*0.6])
print "70% Bucket:",len([a for a in area_np if a >= max(area_np)*0.6  and a < max(area_np)*0.7])
print "80% Bucket:",len([a for a in area_np if a >= max(area_np)*0.7  and a < max(area_np)*0.8])
print "90% Bucket:",len([a for a in area_np if a >= max(area_np)*0.8  and a < max(area_np)*0.9])
print "100% Bucket:",len([a for a in area_np if a >= max(area_np)*0.9])

#mergedContours = [contour for contour in mergedContours if xy_area(contour) > 1*3.14*px_mm and xy_area(contour) < 5*3.14*px_mm]
#mergedContours = [contour for contour in mergedContours if cv2.contourArea(contour) > 1*px_mm and cv2.contourArea(contour) < 5*px_mm]
mergedContours = [contour for contour in mergedContours if xy_area(contour) > 1*px_mm and xy_area(contour) < 25*px_mm]

print "Final # of mergedContours:", len(mergedContours)

for i in range(0, len(mergedContours)):
    r = 255 if i % 3 == 0 else 0
    g = 255 if i % 3 == 1 else 0
    b = 255 if i % 3 == 2 else 0
    cv2.drawContours(img, mergedContours, i, (r,g,b), 1)

cv2.imwrite(cwd+'/contour_overlay/IMG_4465_zoom_contour.jpg', img)
