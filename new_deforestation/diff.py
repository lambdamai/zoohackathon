import cv2
import numpy as np
import matplotlib.pyplot as plt
import tifffile as t
from skimage import color
from skimage import io

def ps_like_diff(img1, img2):
    img1_ = img1.astype(int)
    img2_ = img2.astype(int)
    diff = img1_ - img2_
    return (np.abs(diff)).astype('uint8')

def differences(img1, img2):
    image1=t.imread(img1)
    thresh1 = cv2.cvtColor( image1, cv2.COLOR_BGR2GRAY)
    #hsv = cv2.cvtColor( image1, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    #thresh1 = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
    image2=t.imread(img2)
    thresh2 = cv2.cvtColor( image2, cv2.COLOR_BGR2GRAY )
    #hsv = cv2.cvtColor( image2, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    #thresh2 = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
    diff = ps_like_diff(thresh1, thresh2)
    for idx, x in enumerate(diff):
        for idy, y in enumerate(x):
            if y > 25:
                pass
            else:
                diff[idx][idy] = 0
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    closed1 = cv2.morphologyEx(diff, cv2.MORPH_OPEN, kernel)
    t.imsave('output/diff.tif', closed1)
    
#differences('data/1152_34.tif', 'data/1152_35.tif')
