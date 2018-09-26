# forestry-cv-research

## Log

### Week 1
Vinay: Ran an edge detector on tree cross section. Took contours. Mixed results, able to detect parts of rings, but lots of noise as well.

### Week 2
Vinay: Ran Hough Circle detection on original image as well as on contoured image. Took infeasibly long to run. Ran a closing algorithm on contoured image in an attempt to complete the gaps in the tree rings. Not particularly helpful.

### Week 3
Vinay: Took 8 cross 15 pixel wide slices of the image in a 40 degree arc, each 5 degrees apart. Ran an edge detector on each and contoured individually. Vertically stacked slices and ran a sliding window across the resulting imaging, collecting "votes" for whether each slice was able to yield a ring there. Need to figure out how to tune parameters -- it seems like results vary pretty wildly between cross sections, may not be a good correlation with whre the rings actually exist.
