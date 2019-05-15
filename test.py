# -*- coding: utf-8 -*-
"""
Created on Thu May  9 23:10:53 2019
调用本目录下其他文件的函数
@author: zhenyu

"""

import cv2
import numpy as np
import datetime
from gray import gray
from filters import lp2

if __name__ == '__main__':

    starttime = datetime.datetime.now()
    
    orgimg_path =  r"D:\zhenyu_coding_test\Lena.jpg"
    orgimg = cv2.imread(orgimg_path)
    cv2.imshow("orgimg",orgimg)
    
    grayimg = gray(orgimg)
    cv2.imshow("grayimg",grayimg)
    
    lp2img = lp2(grayimg)
    cv2.imshow("lp2img",lp2img)


    
    endtime = datetime.datetime.now()
    t =str((endtime - starttime).seconds)
    print( "The programming running costs time is:"+t+"s")
     
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()