# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:28:06 2019

@author: zhenyu
"""
import numpy as np
import cv2



def ReplaceImg(imgPath,a1 = 200,a2 =255 ,b1 = 100,b2 = 180,c1 =30 ,c2 =100 ):
    
    
    img = cv2.imread(imgPath)
    width,height,channels = img.shape
    
    for i in range(width):
        for j in range(height):
            if((img[i][j][0] >= a1) and (img[i][j][0] <= a2) and 
               (img[i][j][1] >= b1) and (img[i][j][1] <= b2) and 
               (img[i][j][2] >= c1) and (img[i][j][2] <= c2) ):
                img[i][j] = (255,255,255)
        
    #cv2.imwrite(r"D:\zhenyu_coding_test\replace_Lena.jpg", img)
    cv2.imshow("img",img)        
if __name__ == "__main__":
    imgPath = r"D:\zhenyu_coding_test\img.jpg"
    ReplaceImg(imgPath)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    
    
    
            