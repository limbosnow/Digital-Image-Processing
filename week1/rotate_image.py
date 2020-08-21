#3、Rotate the image by 45 and 90 degrees (Matlab provides simple command lines for doing this).//旋转图像

import cv2 as cv
img=cv.imread('./images/src.jpg',0)
cols=img.shape[1]
rows=img.shape[0]
M=cv.getRotationMatrix2D((cols / 2,rows / 2), 45,0.5)
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('rotate',dst)
M1=cv.getRotationMatrix2D((cols / 2,rows / 2), -45,2)
dst2=cv.warpAffine(dst, M1, (cols, rows))
cv.imshow('rotate_back',dst2)
difference=dst2-img
cv.imshow('difference',difference)
cv.waitKey(0)
cv.imwrite('./images/test/difference.jpg',difference)