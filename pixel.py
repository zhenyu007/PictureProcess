# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:17:33 2019
基于像素操作的实验程序
@author: zhenyu
"""
import datetime
import cv2
import numpy as np
#from PIL import Image

def gray(orgimg):
    
    grayimg = list()
    
    for i in range(weight):
        for j in range(height):
            grayimg.append(np.uint8(0.299*orgimg[i][j][0] + 0.587*orgimg[i][j][1] + 0.114*orgimg[i][j][2]))
            
    grayimg = np.array(grayimg).reshape(weight,height)
    
    return grayimg

def lp2img(img,  a=0,b=1,c=0,  d=1,e=-4,f=1,  g=0,h=1,k=0):
    
    lp2img = list()
    
    for m in range(1,weight-1):
        for n in range(1,height-1):
            lp2img.append(np.uint8(abs(
            img[m-1][n-1]*a + img[m-1][n]*b + img[m-1][n+1]*c + 
            img[m][n-1]*d + img[m][n]*e + img[m][n+1]*f + 
            img[m+1][n-1]*g+ img[m+1][n]*h + img[m+1][n+1]*k)))
            
    
    lp2img = np.array(lp2img).reshape(weight-2,height-2)
    
    return lp2img

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    orgimg_path =  r"D:\zhenyu_coding_test\Lena.jpg"
    '''   r"D:\zhenyu_coding_test\apple.jpg"   '''
    orgimg = cv2.imread(orgimg_path)
    weight = orgimg.shape[0]
    height = orgimg.shape[1]
    cv2.imshow("orgimg",orgimg)
    
    grayimg = gray(orgimg)
    cv2.imshow("grayimg",grayimg)
    
    lp2img = lp2img(grayimg,0,-1,0,-1,4,-1,0,-1,0)
    '''for x in range(398):
        for y in range(398):
            if(lp2img[x][y] > 250):
                lp2img[x][y] =255
            else:
                lp2img[x][y] =0'''
  #  lp3img = lp2img(lp2img,0,-1,0,-1,4,-1,0,-1,0)           
                
    cv2.imshow("lp2img",lp2img)
    endtime = datetime.datetime.now()
    t =str((endtime - starttime).seconds)
    print( "The programming running costs time is:"+t+"s")
     
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    