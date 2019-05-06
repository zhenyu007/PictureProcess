# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:17:33 2019

@author: zhenyu
"""

import cv2
import numpy as np
from PIL import Image

if __name__ == '__main__':
    orgimg = cv2.imread(r"D:\zhenyu_coding_test\Lena.jpg")
    grayimg = list()
    for i in range(400):
        for j in range(400):
            grayimg.append(np.uint8(0.299*orgimg[i][j][0] + 0.587*orgimg[i][j][1] + 0.114*orgimg[i][j][2]))
            
    grayimg = np.array(grayimg).reshape(400,400)
   # grayimg = Image.fromarray(grayimg)
    cv2.imshow("grayimg",grayimg)
    
    '''
    img = list()
    for i in range(200):
        for j in range(200):
            img.append(orgimg[2*i][2*j])
    img= np.array(img).reshape(200,200)   
    #img = np.array(img)
    cv2.imshow("img",img)
    print(img)
    '''
    print(type(grayimg))
    print(type(orgimg))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    