# -*- coding: utf-8 -*-
"""
Created on Thu May  2 20:57:46 2019

@author: zhenyu
"""

import cv2
import numpy as np

def stretch(img):
    max = float(img.max()) 
    min = float(img.min())
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = (255/(max-min))*img[i,j]-(255*min)/(max-min)
        return img
             

if __name__ == '__main__':
    imgpath = r"D:\zhenyu_coding_test\Lena.jpg" 
    
    orgimg = cv2.imread(imgpath)
    print("图片读入成功！")
    cv2.imshow("Lena",orgimg)
    
    grayimg = cv2.cvtColor(orgimg, cv2.COLOR_BGR2GRAY)
    print("灰度处理成功！")
    cv2.imshow("Gray_Lena",grayimg)
    
    
    reimg =cv2.resize(grayimg,(100,100))
    cv2.imshow("Re_Lena",reimg)
    
    print(reimg.shape)
    cv2.imwrite(r"D:\zhenyu_coding_test\RE_Lena.jpg", reimg)

    
    cv2.waitKey(0)
    cv2.destroyAllWindows()