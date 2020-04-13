# Stereo-to-Depth_Image_Manipulation
A Python script implementation in Computing a depth map from stereo images and manipulations using OpenCV.

This script explains how to create depth map from stereo images. It takes a raw input image(s)
 and gives out the final resized output image in depth form.
 
# Explanation;
First, in order to run this scrpit, you will need a set of stereo images:
#              >>imgL and,
#              >>imgR, 
from the OpenCV doumentations tutorial which can be found here; 
#                                         https://docs.opencv.org/3.1.0/d3/d14/tutorial_ximgproc_disparity_filtering.html


So by comparing these two images, disparity map can be computed which, for this stereo pair cointains differences
 in horizontal coordinates of corresponding points. Values in disparity map are inversely proportional to the scene depth.

Stereo vision is similar to human binocular vision. Objets which are closer to our eyes have larger relative shift, then the ones further away.
