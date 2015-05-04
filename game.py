# -*- coding: cp936 -*-

import pygame
from sys import exit
from pygame.locals import *

##import cv2
##import numpy


#初始化pygame,为使用硬件做准备
pygame.init()
#创建了一个窗口,窗口大小和背景图片大小一样
screen = pygame.display.set_mode((666, 500), 0, 32) 
#设置窗口标题
pygame.display.set_caption("Hello, World!")
#加载并转换图像
background1 = pygame.image.load('py1.png').convert()
background2 = pygame.image.load('py2.png').convert()
pic=1
background = background1


# try for the cv2
##img = cv2.imread('white.png')
##print img.shape
##
##print img


rec = (10,10,100,200)


#设置全屏

Fullscreen = False


#游戏主循环
while True:
       for event in pygame.event.get():
              #接收到退出事件后退出程序
              if event.type == pygame.QUIT:
                     pygame.quit()
                     exit()
              #接受鼠标按下的事件
              if event.type == pygame.MOUSEBUTTONDOWN:
                     if pic==1:
                            background = background1
                            pic=2
                     else:
                            background = background2
                            pic=1
              if event.type == KEYDOWN:
                     if event.key == K_f:
                            Fullscreen = not Fullscreen
                            if Fullscreen:
                                   screen = pygame.display.set_mode((666, 500), FULLSCREEN, 32)
                            else:
                                   screen = pygame.display.set_mode((666, 500), 0, 32) 
                            
                     
              
                     
       #将背景图画上去
       screen.blit(background, (0,0))
       pygame.draw.ellipse(screen,(0,0,255),rec)
       pygame.draw.line(screen,(255,255,255),(200,200),(400,400),5)
       
       #刷新一下画面
       pygame.display.update()






