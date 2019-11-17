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

def differences():
    for i in range(1,35):
        image1=t.imread("1152_{}.tif".format(i))
        thresh1 = cv2.cvtColor( image1, cv2.COLOR_BGR2GRAY)
    #hsv = cv2.cvtColor( image1, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    #thresh1 = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
        image2=t.imread("1152_{}.tif".format(i+1))
        thresh2 = cv2.cvtColor( image2, cv2.COLOR_BGR2GRAY )
    #hsv = cv2.cvtColor( image2, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV
    #thresh2 = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
        diff = ps_like_diff(thresh1, thresh2)
        t.imsave('dif_{}.tif'.format(i), diff)
    
differences()
