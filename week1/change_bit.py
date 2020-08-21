#1、Write a computer program capable of reducing the number of intensity levels in an image from 256 to 2,
# in integer powers of 2. The desired number of intensity levels needs to be a variable input to your program.改变存储位深

# 1 读取图片的二维数组  定义新的灰度存储方式，比如0～255不再是8分为256份，而是16份 然后显示
import cv2 as cv
n=16
img=cv.imread('./images/src.jpg',0)
cv.imshow('original',img)
#这一步就是在改变位深，原来0～255有256个值，8bit，若n=16，0～15，16~31...240~255这样16个级别，0～15都是0，16～31都是16，变成4bit
img=img//n*n
cv.imshow('grayscale',img)
cv.imwrite('./images/test/change_bit.jpg',img)
cv.waitKey(0)

































