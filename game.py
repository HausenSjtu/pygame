# -*- coding: cp936 -*-

import pygame
from sys import exit


#初始化pygame,为使用硬件做准备
pygame.init()
#创建了一个窗口,窗口大小和背景图片大小一样
screen = pygame.display.set_mode((1000, 750), 0, 32) 
#设置窗口标题
pygame.display.set_caption("Hello, World!")
#加载并转换图像
background1 = pygame.image.load('py1.png').convert()
background2 = pygame.image.load('py2.png').convert()
pic=1
background = background1


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
                            
                     
              
                     
       #将背景图画上去
       screen.blit(background, (0,0))
       
       #刷新一下画面
       pygame.display.update()






