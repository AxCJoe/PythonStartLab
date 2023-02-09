import cv2
import os.path
import glob
import numpy as np
def img_cut_multiple(jpgfile,outdir):
    img=cv2.imread(jpgfile,cv2.IMREAD_ANYCOLOR)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgInfo=img.shape
    height=imgInfo[0]
    width=imgInfo[1]
    pts1 = np.float32([[0,0],[0,height-1],[width-1,height-1],[width-1,0]])
    pts2 = np.float32([[300,300],[0,height-1],[width-100,height-100],[width-1,0]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (2500, 2500))

    cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), dst)


for jpgfile in glob.glob(r'C:\Users\Joker\Desktop\DL\aa\y\*.jpg'):
    img_cut_multiple(jpgfile, r'C:\Users\Joker\Desktop\cv2')
