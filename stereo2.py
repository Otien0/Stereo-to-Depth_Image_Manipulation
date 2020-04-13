import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# my_image = cv2.imread('image1.jpg')
# show_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2HSV)
#
# my_image2 = cv2.imread('image2.jpg')
# show_image2 =cv2.cvtColor(my_image2, cv2.COLOR_BGR2HSV)
#
# my_image3 = cv2.imread('image3.jpg')
# show_image3 = cv2.cvtColor(my_image3, cv2.COLOR_BGR2HSV)
# plt.imshow(show_image)

def display_img(img,cmap=None):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap)

img = cv2.imread('Left_image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
height, width = img.shape[:2]
imgL = img[0:height//2, 0:width]
imgR = img[height//2:height, 0:width]
img2 = cv2.imwrite("Left2.png", img)
display_img(img)

img = cv2.imread('Left_image.jpg',0)
height, width = img.shape[:2]
imgL = img[0:height//2, 0:width]
imgR = img[height//2:height, 0:width]
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
mg2 = cv2.imwrite("Left3.png", img)
display_img(thresh1,cmap='gray')

img = cv2.imread('Left_image.jpg')
height, width = img.shape[:2]
imgL = img[0:height//2, 0:width]
imgR = img[height//2:height, 0:width]
img = cv2.cvtColor(img, cv2.COLOR_RGB2HLS_FULL)
img2 = cv2.imwrite("Left4.png", img)
display_img(img)

kernel = np.ones(shape=(4,4),dtype=np.float32)/10
kernel
img = cv2.imread('Left_image.jpg')
height, width = img.shape[:2]
imgL = img[0:height//2, 0:width]
imgR = img[height//2:height, 0:width]
img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV_FULL)
dst = cv2.filter2D(img,-1,kernel)
img2 = cv2.imwrite("Left5.png", img)
display_img(dst)

img = cv2.imread('Left_image.jpg',0)
height, width = img.shape[:2]
imgL = img[0:height//2, 0:width]
imgR = img[height//2:height, 0:width]
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
img2 = cv2.imwrite("Left6.png", img)
display_img(sobelx,cmap='gray')

if __name__ == '__main__':
    print("Stereo-to-Depth-manipulations")
