# forestry-cv-research

## Log

### Week 1
Vinay: Ran an edge detector on tree cross section. Took contours. Mixed results, able to detect parts of rings, but lots of noise as well.

William: Ran Canny-Edge Detection and then found contours from binary image produced from edge detection. Results were poor, only half of objects were detected, and many contours recognized negative space or reflections.

### Week 2
Vinay: Ran Hough Circle detection on original image as well as on contoured image. Took infeasibly long to run. Ran a closing algorithm on contoured image in an attempt to complete the gaps in the tree rings. Not particularly helpful.

William: Used less dense source image, and analyzed a smaller sub section for clearer results. Updated Canny Edge detection min/max values to capture more edges, however too many edges now and need to be filtered.

### Week 3
Vinay: Took 8 cross 15 pixel wide slices of the image in a 40 degree arc, each 5 degrees apart. Ran an edge detector on each and contoured individually. Vertically stacked slices and ran a sliding window across the resulting imaging, collecting "votes" for whether each slice was able to yield a ring there. Need to figure out how to tune parameters -- it seems like results vary pretty wildly between cross sections, may not be a good correlation with whre the rings actually exist.

William: Found the area of each contour, first using cv.contourArea() but had problems since many contours are sparse in width but have are long, so found rectangular area. Also implemented an overlapping function to prevent contours from stacking on each others' space. Finally, found statistics and buckets on the area of all the final pruned contours.