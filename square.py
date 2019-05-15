# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:38:33 2019

@author: zhenyu
"""

import cv2
import numpy as np


if __name__ == '__main__':

    
    
    #orgimg_path =  r"D:\zhenyu_coding_test\two_value_apple.jpg"
    #orgimg = cv2.imread(orgimg_path,-1)
    
    img = cv2.imread(r"D:\zhenyu_coding_test\two_value_apple.jpg")
    
    cv2.rectangle(img, (10, 10), (100, 100), (0, 255, 0), 2)
    print(img.shape)
    
    
    
    cv2.imshow("orgimg",img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()