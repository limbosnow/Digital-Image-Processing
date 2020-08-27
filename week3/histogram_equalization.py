#Implement a histogram equalization function.
# If using Matlab, compare your implementation with Matlab’s built-in function.
'''
•统计原始图像中各个灰度值出现的概率
•生成映射函数
•逐个映射图中的灰度
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(img):
    H,W,C=img.shape
    S=H*W*C
    L=255
    total=0
    out=img.copy()
    #np.where()此时返回索引值
    for l in range(1,L):
        num=np.where(img == l)
        total+=len(img[num])
        S_value=L*total/S
        out[num]=S_value
    return out
img=cv2.imread("./imori.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
out=histogram_equalization(img)
out2=cv2.equalizeHist(gray_img)
fig=plt.figure(1,figsize=[10,5])
ax1=plt.subplot(121)
ax2=plt.subplot(122)
ax1.hist(img.ravel(),255,[0,255],rwidth=1)
ax2.hist(out.ravel(),255,[0,255],rwidth=1)
plt.show()
cv2.imshow("equalization",np.hstack([img,out]))
cv2.imshow("out2",out2)
cv2.waitKey(0)









