#4、For every 3×3 block of the image (without overlapping), replace all corresponding 9 pixels by their average.
# This operation simulates reducing the image spatial resolution. Repeat this for 5×5 blocks and 7×7 blocks.
# If you are using Matlab, investigate simple command lines to do this important operation.
import cv2
import numpy as np

def mean_filter_without_overlapping(image,K_size=9):
    if len(image.shape)==3:
        H,W,C=image.shape
    else:
        image=np.expand_dims(image,axis=-1)
        H,W,C=image.shape

    #zero padding
    pad_H=0 if H % K_size == 0 else K_size-H % K_size
    pad_W=0 if W % K_size == 0 else K_size-W % K_size
    out=np.zeros((H+pad_H,W+pad_W,C),dtype=np.float)
    out[pad_H:pad_H+H,pad_W:pad_W+W]=image.copy().astype(np.float)

    #Kernel
    K=np.ones((K_size,K_size),dtype=np.float)
    K/=np.sum(K)

    #filter
    tmp=out.copy()
    for y in range(0,H+pad_H,K_size):
        for x in range(0,W+pad_W,K_size):
            for c in range(C):
                out[y:y+K_size,x:x+K_size,c]=np.sum(K*tmp[y:y+K_size,x:x+K_size,c])
    out=out[pad_H:pad_H+H,pad_W:pad_W+W].astype(np.uint8)
    return out
image=cv2.imread("./images/2.jpg")
out=mean_filter_without_overlapping(image)
cv2.imshow("out",out)
cv2.waitKey(0)

