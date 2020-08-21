#1、Write a computer program capable of reducing the number of intensity levels in an image from 256 to 2,
# in integer powers of 2. The desired number of intensity levels needs to be a variable input to your program.改变存储位深
#4、For every 3×3 block of the image (without overlapping), replace all corresponding 9 pixels by their average.
# This operation simulates reducing the image spatial resolution. Repeat this for 5×5 blocks and 7×7 blocks.
# If you are using Matlab, investigate simple command lines to do this important operation.


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


#4
# import cv2 as cv
# img=cv.imread('./images/src.jpg',0)
# img=cv.resize(img,(300,300))
# pixel=[]
# for i in range(0,img.shape[0]-2,3):
#     for j in range(0,img.shape[1]-2,3):
#         pixel1=img[i+1][j+1]
#         for ii in range(i,i+3):
#             for jj in range(j,j+3):
#                     pixel.append(img[ii][jj])
#         pixel1=sum(pixel)/(len(pixel))
#         img[i][j]=pixel1
#         img[i][j+1]=pixel1
#         img[i][j+2]=pixel1
#         img[i+1][j]=pixel1
#         img[i+1][j+1]=pixel1
#         img[i+1][j+2]=pixel1
#         img[i+2][j]=pixel1
#         img[i+2][j+1]=pixel1
#         img[i+2][j+2]=pixel1
# cv.imshow('neiberhood',img)
# print(img)
# cv.waitKey(0)


































