#读取test.jpg图片并显示
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('test.png')
cv2.imshow('image',img)
cv2.waitKey(100)




