import os
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d,Axes3D

#单个图片生成3d直方图
#bins：子区段数目，如果我们统计0255每个像素值，bins=256；如果划分区间，比如015, 1631…240255这样16个区间，bins=16
def process_image_to_3d_histogram(image_path,bins=32):
    print(image_path)
    image=cv.imread(image_path,1)
    image=cv.resize(image,(512,512))
    #channels[1,2,0] mask=None,要计算的区域
    hist=cv.calcHist([image],[1,2,0],None,[bins,bins,bins],[0,255,0,255,0,255])
    return hist


#依次处理文件夹中的多张图片 先将所有图片的像素值都相加 再除以图片的数量
def process_all_images(folder,bins=32):
    count=0
    #创建一个32*32*32的数组矩阵，都填充数字0
    hist=np.zeros((bins,bins,bins))
    #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    for f in os.listdir(folder):
        if f.startswith('.'):
            continue
        #os.path.join路径拼接文件路径
        f=os.path.join(folder,f)
        if os.path.isfile(f):
            single_hist=process_image_to_3d_histogram(f,bins=bins)
            hist+=single_hist
            count+=1
    hist/=count
    return hist


def show_3d_histogram_plot(hist,scale=1000):
    bins=hist.shape[0]
    #生成坐标网格点（0到31的32个数）x,y,z都是32*32*32 
    x,y,z=np.meshgrid(np.arange(bins),np.arange(bins),np.arange(bins))
    #先是把矩阵转置，接着reshape(-1,3)指定数组列为3，再转置？
    #方法1
    index=np.stack([x,y,z],axis=-1).reshape(-1,3).transpose()
    x=index[0]
    y=index[1]
    z=index[2]
    #方法2
    # x=x.flatten()
    # y=y.flatten()
    # z=z.flatten()
    # index=np.array([x,y,z])

    #行设定为1
    s=hist.reshape(-1)
    #求范数，lina表示linear线性，norm表示范数
    s=s/np.linalg.norm(s)
    s=s*scale

    #（0，1）
    c = index.transpose()/bins

    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    #（0，1）
    ax.scatter(x/bins,y/bins,z/bins,c=c,s=s)
    ax.set_xlabel('R')
    ax.set_ylabel('G')
    ax.set_zlabel('B')
    plt.show()

if __name__=='__main__':
    folder='./images/Japan'
    hist=process_all_images(folder,bins=16)
    show_3d_histogram_plot(hist)













