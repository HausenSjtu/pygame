import cv2
import numpy
import time


img1 = cv2.imread('py1.png')
##cv2.imshow('zhsimg',img1)

print img1.shape
print img1.size

##img3=img1.copy()
##dis = (1000,1000,3)
##img3.resize(dis)
##cv2.imshow('zhsimg2',img2)

img2 = cv2.imread('py2.png')

  
##cv2.namedWindow("zhsimg")
##cv2.waitKey(0)

##for i in range(5):
##    cv2.imshow('zhsimg',img2)
##    cv2.waitKey(0)
##    time.sleep(1)
##    cv2.imshow('zhsimg',img1)
##    cv2.waitKey(0)

##imgtmp =img1.copy()
##for i in range(3):
##    cv2.imshow('zhsimg',imgtmp)
####    cv2.waitKey(0)
##    time.sleep(1)
##    imgtmp = img2.copy()

l = [1,2,3]
i=0
print eval('l'+'['+str(i)+']')



