# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:17:33 2019

@author: zhenyu
"""

import cv2
import numpy as np
#from PIL import Image

def gray(orgimg):
    
    grayimg = list()
    
    for i in range(400):
        for j in range(400):
            grayimg.append(np.uint8(0.299*orgimg[i][j][0] + 0.587*orgimg[i][j][1] + 0.114*orgimg[i][j][2]))
            
    grayimg = np.array(grayimg).reshape(400,400)
    
    return grayimg

def lp2img(grayimg,  a=0,b=1,c=0,  d=1,e=-4,f=1,  g=0,h=1,k=0):
    
    lp2img = list()
    
    for m in range(1,399):
        for n in range(1,399):
            lp2img.append(np.uint8(
            grayimg[m-1][n-1]*a + grayimg[m-1][n]*b + grayimg[m-1][n+1]*c + 
            grayimg[m][n-1]*d + grayimg[m][n]*e + grayimg[m][n+1]*f + 
            grayimg[m+1][n-1]*g+ grayimg[m+1][n]*h + grayimg[m+1][n+1]*k))
            
    
    lp2img = np.array(lp2img).reshape(398,398)
    
    return lp2img

if __name__ == '__main__':
    
    orgimg = cv2.imread(r"D:\zhenyu_coding_test\Lena.jpg")
    cv2.imshow("orgimg",orgimg)
    
    grayimg = gray(orgimg)
    cv2.imshow("grayimg",grayimg)
    
    lp2img = lp2img(grayimg,1,1,1,1,-8,1,1,1,1)
    cv2.imshow("lp2img",lp2img)
    
 
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    