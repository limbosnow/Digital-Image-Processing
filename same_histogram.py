#生成同样的直方图 histogram
import cv2
import numpy as np

# def split_big2small(l,num):
#     'l是传入的列表，num是要切成几行'
#     list1=[]
#     for i in range(0,len(l),num):
#         obj=l[i:i+num]
#         list1.append(obj)
#     return list1
#
# img=cv2.imread("./images/2.jpg",0)
# img=cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))
# matrix=img.copy()
# matrix.sort()                 #跟img是同行同列的二维矩阵，但是sort()函数是对每一行单独进行排列，如果想要把整个二维矩阵像素进行排列的话，有函数吗？？？
#
# a=[]
# a=matrix.reshape(0)
# # for i in matrix:
# #     for j in i:
# #         j.astype(np.uint8)
# #         a.append(j)
# a.sort()
# matrix2=split_big2small(a,int(img.shape[1]))
# matrix3=np.array(matrix2).astype(np.uint8)
#
# cv2.imshow("first",img)
# cv2.imshow("1",matrix3)
# cv2.imwrite("./images/src.jpg",img)
# cv2.imwrite("./images/dst.jpg",matrix3)
# cv2.waitKey(0)
#俺那时候真是个傻子捏，这么简单的问题想得那么复杂 ，害害害
img=cv2.imread("./images/2.jpg",0)
img=cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))
print(img.shape)
matrix=img.copy()
a=matrix.reshape(-1)
a.sort()
a.astype('uint8')
a=a.reshape(int(img.shape[0]),int(img.shape[1]))
cv2.imshow("hahaha",a)
cv2.waitKey(0)


