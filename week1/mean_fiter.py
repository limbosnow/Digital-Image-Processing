#2、Using any programming language you feel comfortable with (it is though recommended to use the provided free Matlab),
# load an image and then perform a simple spatial 3x3 average of image pixels.
# In other words, replace the value of every pixel by the average of the values in its 3x3 neighborhood.
# If the pixel is located at (0,0), this means averaging the values of the pixels
# at the positions (-1,1), (0,1), (1,1), (-1,0), (0,0), (1,0), (-1,-1), (0,-1), and (1,-1).//邻域处理
# Be careful with pixels at the image boundaries. Repeat the process for a 10x10 neighborhood and again for a 20x20 neighborhood.
# Observe what happens to the image (we will discuss this in more details in the very near future, about week 3).
import numpy as np
import cv2

def mean_filter(image,K_size=10):
    if len(image.shape)==3:
        H,W,C=image.shape
    else:
        image=np.expand_dims(image,axis=-1)
        H,W,C=image.shape
    #zero padding
    pad=K_size//2
    out=np.zeros((H+pad*2,W+pad*2,C),dtype=np.float)
    out[pad:pad+H,pad:pad+W]=image.copy().astype(np.float)

    #kernel
    K=np.ones((K_size,K_size),dtype=np.float)
    K/=np.sum(K)

    #filter
    tmp=out.copy()
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[y+pad,x+pad,c]=np.sum(K*tmp[y:y+K_size,x:x+K_size,c])

    out=np.clip(out,0,255)
    out=out[pad:pad+H,pad:pad+W]
    out=out.astype(np.uint8)
    return out

img=cv2.imread("./images/2.jpg")
out=mean_filter(img)
cv2.imshow("out",out)
cv2.waitKey(0)

