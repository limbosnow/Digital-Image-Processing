#生成波形图 彩色图的话有三通道的信息。那么亮度是怎么算出来,可以先从RGB色彩空间转换到HSV，用v当亮度信息
#先取出每行的信息，800*1280,先矩阵转置，三维转置？？？(transpose)
import cv2
import numpy as np

img=cv2.imread("./images/2.jpg",1)
hsv_space=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
print(hsv_space.shape)
arr1=hsv_space.transpose(1,0,2)
#按照三维中最小维，也就是像素颜色的最后一位来排序，返回索引值，也就是按照亮度排序，注意我已经转置了
#arr[:,:,-1].argsort()会看成n个二维数组，在每个二维数组之间以像素最后一位排序
b=arr1[:,:,-1].argsort()
print(b.shape)
#根据索引值，重新排序，
for i in range(1280):
   arr1[i]=arr1[i,b[i],:]      #行不变，像素排布不变，列根据索引排列
arr1=arr1.transpose(1,0,2)     #再转置回去
arr1=cv2.cvtColor(arr1,cv2.COLOR_HSV2RGB)     #色彩空间也转回去
cv2.imshow("waveform",arr1)
cv2.waitKey(0)
cv2.imwrite("./images/waveform_test.jpg",arr1)



