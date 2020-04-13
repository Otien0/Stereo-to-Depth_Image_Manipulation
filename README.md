# Stereo-to-Depth_Image_Manipulation
A Python script implementation in Computing a depth map from stereo images and manipulations using OpenCV.

This script explains how to create depth map from stereo images. It takes a raw input image(s)
 and gives out the final resized output image in depth form.
 
# Explanation;
First, in order to run this scrpit, you will need a set of stereo images:
#              >>imgL and,
#              >>imgR
After calibration, and then rectification (which projects images back to a common plane) corresponding image points can be found by minimizing
 cost function, which in simplest case summarise differences in pixels intensities in neighbourhood of two analyzed points.

So by comparing these two images, disparity map can be computed which, for this stereo pair cointains differences in horizontal coordinates of corresponding points. Values in disparity map are inversely proportional to the scene depth.

Stereo vision is similar to human binocular vision. Objets which are closer to our eyes have larger relative shift, then the ones further away.
