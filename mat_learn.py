# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:11:59 2019

@author: zhenyu
"""

import numpy as np
import cv2
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt


img = cv2.imread(r"D:\zhenyu_coding_test\Lena.jpg")
small_img = img[0::4,0::5]
l_img = cv2.resize(small_img,(400,400))
cv2.imshow('small_img',l_img)



M = np.arange(25).reshape(5,5)
N = np.arange(25).reshape(5,5)
C = M[0::4,0::5]  #矩阵切片
print(type(img))
 = np.arange(1,11,2)   #指定步长
c = np.array([[1,2,3],[4,5,6]])
d = c.reshape(2,3)
a = np.arange(0,9).reshape(3,3)
a = np.linspace(1,10,5) #指定数目
A = np.arange(25).reshape(5,5)
I = np.arange(5)
B = np.insert(A,5,I,0)

print(B)


cv2.waitKey(0)
cv2.destroyAllWindows()