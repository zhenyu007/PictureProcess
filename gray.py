# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:51:36 2019

用于将彩色RGB图片转化为灰度图

@author: zhenyu
"""

import numpy as np
import cv2
import datetime

#img为三通道彩色图像
def gray(img):
    
    width,height,channels = img.shape
    
    grayimg = list()
    
    for i in range(width):
        for j in range(height):
            grayimg.append(np.uint8(0.299*img[i][j][0] + 0.587*img[i][j][1] + 0.114*img[i][j][2]))
            
    grayimg = np.array(grayimg).reshape(width,height)
    
    return grayimg


if __name__ == '__main__':

    starttime = datetime.datetime.now()
    
    orgimg_path =  r"D:\zhenyu_coding_test\Lena.jpg"
    orgimg = cv2.imread(orgimg_path)
    grayimg = gray(orgimg)
    cv2.imshow("grayimg",grayimg)
    
    endtime = datetime.datetime.now()
    t =str((endtime - starttime).seconds)
    print( "The programming running costs time is:"+t+"s")
     
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
        