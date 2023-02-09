import cv2
import numpy as np
import os.path
import glob
def img_cut_multiple(jpgfile,outdir):
    img=cv2.imread(jpgfile,cv2.IMREAD_ANYCOLOR)
    #img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgInfo = img.shape
    height = imgInfo[0]
    width = imgInfo[1]
    dst = np.zeros((height,width,3),np.uint8)
    for i in range(0,height):
        for j in range(0,width):
            (b,g,r) = img[i,j]
            bb = int(b)+50
            gg = int(g)+50
            rr = int(r)+50
            if bb>255:
                bb = 255
            if gg>255:
                gg = 255
            if rr>255:
                rr = 255
            dst[i,j] = (bb,gg,rr)
    cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), dst)

for jpgfile in glob.glob(r'C:\Users\Joker\Desktop\DL\aa\*.jpg'):
    img_cut_multiple(jpgfile, r'C:\Users\Joker\Desktop\cv2')
