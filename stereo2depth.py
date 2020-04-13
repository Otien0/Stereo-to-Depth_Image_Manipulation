import cv2
import numpy as np
import os
import sys
import glob


path = r"/home/net/MORYSO/Assignment/stereo2depth/Input_images*.*"

print('loading images...')
pathname = os.path.dirname(sys.argv[0])

# filename = os.path.splitext(os.path.basename(sys.argv[0]))[0]
filename = r'/home/net/MORYSO/stereo2depth/stero2depth.py'
print('Loading images from :' + path)

for image, file in enumerate(glob.glob(path)):
    print(image, file)
    a = cv2.imread(file)
    #print(a)
    img = cv2.imread(file)
    assert not isinstance(img, type(None)), 'image not found'
    c = img
    cv2.imshow('Depth Image', c)
    cv2.imwrite('/home/net/MORYSO/Assignment/stereo2depth/Output_Images/output_image{}.png'.format(image), c)

    height, width = img.shape[:2]
    imgL = img[0:height//2, 0:width]
    imgR = img[height//2:height, 0:width]

    window_size = 3
    shouldirun = ()
    def Nothing(value):
        if (shouldirun == 1):
            Update(0)
        else:
                return None

    def Update(value):
        miniDisparities=16
        window_size = cv2.getTrackbarPos('windowSize','settings')
        rez = cv2.getTrackbarPos('resolution','settings')/20.0
        resL = cv2.resize(imgL,None,fx=rez, fy=rez, interpolation = cv2.INTER_AREA)
        resR = cv2.resize(imgR,None,fx=rez, fy=rez, interpolation = cv2.INTER_AREA)

        match_left = cv2.StereoSGBM_create(
            miniDisparity=0,
            numDisparities=miniDisparities,
            blockSize= cv2.getTrackbarPos('blockSize', 'settings'),
            P1=8 * 3 * window_size ** 2,
            P2=32 * 3 * window_size ** 2,
            disp12MaxDiff=1,
            uniquenessRatio=15,
            speckleWindowSize=0,
            speckleRange=2,
            preFilterCap= cv2.getTrackbarPos('preFilterCap','settings'),
            mode=cv2.STEREO_SGBM_MODE_HH
            )

        match_right = cv2.ximgproc.createRightMatcher(match_left)

        # FILTER parameters
        lmbda = cv2.getTrackbarPos('lmbda','settings') * 1000
        sigma = 1.2
        visual_multiplier = 1

        wls_filter = cv2.ximgproc.createDisparityWLSFilter(left_match=match_left)
        wls_filter.setLambda(lmbda)
        wls_filter.setSigmaColor(sigma)

        if (value == 0):
            print('calculating depth map')
        displ = match_left.compute(resL, resR)
        dispr = match_right.compute(resR, resL)
        imgLb = cv2.copyMakeBorder(imgL, top=0, bottom=0, left=np.uint16(minDisparities/rez), right=0, borderType= cv2.BORDER_CONSTANT, value=[155,155,155] )
        filteredImg = wls_filter.filter(disp1, imgLb, None, dispr)
        filteredImg = filteredImg + (cv2.getTrackbarPos('Bright','settings')-100)
        filteredImg = (cv2.getTrackbarPos('Contrast','settings')/10.0)*(filteredImg - 128) + 128
        filteredImg = np.clip(filteredImg, 0, 255)
        filteredImg = np.uint8(filteredImg)
        filteredImg = cv2.resize(filteredImg,(width,height/2),inerpolation = cv2.INTER_CUBIC)
        filteredImg = filteredImg[0:height, np.uint16(minDisparities/rez):width]
        filteredImg = cv2.resize(filteredImg, (width,height/2), interpolation = cv2.INTER_CUBIC)

        cv2.imshow('Depth Map', filteredImg)
        cv2.resizeWindow('Depth Map', 1000,500)
        if (value == 1):
            return filteredImg

        def SaveDepth(value):
            if (shouldirun == 1 & value == 1):
                cv2.imwrite(pathname + '/' + filename + '_44.jpg', Update(1), [cv2.IMWRITE_JPEG_QUALITY, 100])
                cv2.imshow('Depth Image', c)
                cv2.imwrite('/home/net/MORYSO/Assignment/stereo2depth/Output_Images/output_image{}.png'.format(image),c)
                cv2.setTrackbarPos('Save Depth','settings',0)


        def Save6DoF(value):
            if(shouldirun == 1 & value == 1):
                depth = Update(1)
                depth = cv2.cvtColor(depth, cv2.COLOR_RGB2HSV)
                dof = np.concatenate((imgR, depth), axis=0)
                cv2.imwrite(pathname + '/' + filename + '_6DoF.jpg', dof, [cv2.IMWRITE_JPEG_QUALITY, 100])
                cv2.imshow('Depth Image', c)
                cv2.imwrite('/home/net/MORYSO/Assignment/stereo2depth/Output_Images/output_image{}.png'.format(image),c)
            cv2.setTrackbarPos('Save 6DoF','settings',0)


        shouldirun = 0
        cv2.namedWindow('Depth Map', cv2.WINDOW_NORMAL)
        cv2.namedWindow('settings', cv2.WINDOW_AUTOSIZE)
        cv2.resizeWindow('settings', 500,400)
        cv2.namedWindow('Left', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Left', 300,150)
        cv2.namedWindow('Right', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Right', 300,150)
        cv2.imshow('Left', imgL)
        cv2.imshow('Right', imgR)
        cv2.createTrackbar('resolution','settings',1,20,Nothing)
        cv2.setTrackbarPos('resolution','settings',1)
        cv2.createTrackbar('blockSize','settings',0,25,Nothing)
        cv2.setTrackbarPos('blockSize','settings',5)
        cv2.createTrackbar('windowSize','settings',0,15,Nothing)
        cv2.setTrackbarPos('windowSize','settings',5)
        cv2.createTrackbar('preFilterCap','settings',0,100,Nothing)
        cv2.setTrackbarPos('preFilterCap','settings', 63)
        cv2.createTrackbar('lmbda','settings',0,100,Nothing)
        cv2.setTrackbarPos('lmbda','settings',80)
        cv2.createTrackbar('Bright','settings',0,200,Nothing)
        cv2.setTrackbarPos('Bright','settings',100)
        cv2.createTrackbar('Contrast','settings',0,30,Nothing)
        cv2.setTrackbarPos('Contrast','settings',10)
        cv2.createTrackbar('Save Depth','settings',0,1,SaveDepth)
        cv2.createTrackbar('Save 6DoF','settings',0,1,Save6DoF)
        shouldirun = 1
        Update(0)


        while(1):
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
        cv2.destroyAllWindows()

    if __name__ == '__main__':
        #try:
        Nothing(0)
        #except (NameError, cv2.error):
        Update(1)
