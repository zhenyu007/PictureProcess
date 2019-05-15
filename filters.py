# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:56:22 2019

@author: zhenyu
"""
import cv2
import datetime
import numpy as np

def lp2(img,  a=0,b=1,c=0,  d=1,e=-4,f=1,  g=0,h=1,k=0):
    
    width,height = img.shape
    
    lp2img = list()
    
    for m in range(1,width-1):
        for n in range(1,height-1):
            lp2img.append(np.uint8(abs(
            img[m-1][n-1]*a + img[m-1][n]*b + img[m-1][n+1]*c + 
            img[m][n-1]*d + img[m][n]*e + img[m][n+1]*f + 
            img[m+1][n-1]*g+ img[m+1][n]*h + img[m+1][n+1]*k)))
            
    
    lp2img = np.array(lp2img).reshape(width-2,height-2)
    
    return lp2img

if __name__ == '__main__':

    starttime = datetime.datetime.now()
    
    orgimg_path =  r"D:\zhenyu_coding_test\RE_Lena.jpg"
    orgimg = cv2.imread(orgimg_path,-1)
    lp2img = lp2(orgimg)
    cv2.imshow("lp2img",lp2img)
    
    endtime = datetime.datetime.now()
    t =str((endtime - starttime).seconds)
    print( "The programming running costs time is:"+t+"s")
     
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
