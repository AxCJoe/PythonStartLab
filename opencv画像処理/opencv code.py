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


#回転処理
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

    matRotate = cv2.getRotationMatrix2D((height*0.5,width*0.5),45,0.5)
    dst = cv2.warpAffine(img,matRotate,(height,width))
    cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), dst)


for jpgfile in glob.glob(r'C:\Users\Joker\Desktop\DL\aa\j\*.jpg'):
    img_cut_multiple(jpgfile, r'C:\Users\Joker\Desktop\cv2')

#射影変換処理

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


#ガンマ補正処理
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

#グレースケール処理

import cv2
import os.path
import glob
import numpy as np
def img_cut_multiple(jpgfile,outdir):
    img=cv2.imread(jpgfile,cv2.IMREAD_ANYCOLOR)
    imgInfo=img.shape
    height=imgInfo[0]
    width=imgInfo[1]

  
    dst = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), dst)


for jpgfile in glob.glob(r'C:\Users\Joker\Desktop\DL\aa\*.jpg'):
    img_cut_multiple(jpgfile, r'C:\Users\Joker\Desktop\cv2')


#アフィン変換処理
import cv2
import os.path
import glob
import numpy as np
def img_cut_multiple(jpgfile,outdir):
    img=cv2.imread(jpgfile,cv2.IMREAD_ANYCOLOR)
    #img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgInfo=img.shape
    height=imgInfo[0]
    width=imgInfo[1]
    matSrc = np.float32([[0,0],[0,height-1],[width-1,0]])
    matDst = np.float32([[50,50],[300,height-200],[width-300,100]])
    matAffine = cv2.getAffineTransform(matSrc,matDst)
    dst = cv2.warpAffine(img,matAffine,(width,height))
    cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), dst)

for jpgfile in glob.glob(r'C:\Users\Joker\Desktop\DL\aa\f\*.jpg'):
    img_cut_multiple(jpgfile, r'C:\Users\Joker\Desktop\cv2')


#バイラテラルフィルタ処理
import cv2
import os.path
import glob

def img_cut_multiple(jpgfile,outdir):
    img=cv2.imread(jpgfile,cv2.IMREAD_ANYCOLOR)
    #img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgInfo=img.shape
    height=imgInfo[0]
    width=imgInfo[1]
    dst = cv2.bilateralFilter(img,30,35,35)
    cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), dst)
    

for jpgfile in glob.glob(r'C:\Users\Joker\Desktop\DL\aaa\*.jpeg'):
    img_cut_multiple(jpgfile, r'C:\Users\Joker\Desktop\cv2')

