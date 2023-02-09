#並進処理
import cv2
import os.path
import glob
import numpy as np
def img_cut_multiple(jpgfile,outdir):
    img=cv2.imread(jpgfile,cv2.IMREAD_ANYCOLOR)
    #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgInfo=img.shape
    height=imgInfo[0]
    width=imgInfo[1]
    dst = np.zeros(img.shape,np.uint8)
    height = imgInfo[0]
    width = imgInfo[1]
    for i in range(0,height-200):
        for j in range(0,width-200):
            dst[i+200,j+200]=img[i,j]
    
    cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), dst)


for jpgfile in glob.glob(r'C:\Users\Joker\Desktop\DL\aa\*.jpg'):
    img_cut_multiple(jpgfile, r'C:\Users\Joker\Desktop\cv2')
