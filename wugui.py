# -*- coding: cp936 -*-

import pygame
from pygame.locals import *
#导入pygame库
from sys import exit
#向sys模块借一个exit函数用来退出程序
pygame.init()
#初始化pygame,为使用硬件做准备



class Tortoise:
    def __init__(self,num):
        self.x = 250
        self.y = 100 -10 *num
        self.zoomdx = (0.2*num+0.2)
        self.zoomdy = (0.05*num+0.05)
        #0:big   1:small   -1:end
        self.zoomFlag = 1
        #0: not start    1: moving   -1:end
        self.moveFlag = 0
        self.visible = False
        self.width = 400
        self.height = 100
        self.maxWidth = self.width
        self.maxHeight = self.height
        self.minWidth = self.maxWidth/2
        self.minHeight = self.maxHeight/2
        self.rec = [self.x - self.width/2, self.y - self.height/2, self.width, self.height]
        self.col = [(num%3==0)*255,(num%3==1)*255,(num%3==2)*255]

    def move(self, button):
        if self.moveFlag == 1:
            self.rec[1] += 3
            if self.rec[1]+self.height > button:
                self.rec[1] = button-self.height
                self.moveFlag = -1

    def zoom(self):
        if self.zoomFlag == 0:
            self.height += self.zoomdy
            self.width += self.zoomdx
            if self.height >= self.maxHeight:
                self.height = self.maxHeight
                self.width = self.maxWidth
                self.zoomFlag = 1
        if self.zoomFlag == 1:
            self.height -= self.zoomdy
            self.width -= self.zoomdx
            if self.height <= self.minHeight:
                self.height = self.minHeight
                self.width = self.minWidth
                self.zoomFlag = 0
        self.rec = [self.x - self.width/2, self.y - self.height/2, self.width, self.height]
        





screen = pygame.display.set_mode((500, 500), 0, 32)
#创建了一个窗口,窗口大小和背景图片大小一样
pygame.display.set_caption("Hello, World!")
#设置窗口标题
background = pygame.image.load('white.png').convert()
once_more = pygame.image.load("once_more.png").convert()
#加载并转换图像

font = pygame.font.Font(None, 32)
times = 0

#surface
#bland_surface = pygame.Surface((100,100))
sur = pygame.surface.Surface((200, 200))


#parameter
result="playing"
Fullscreen = False

#num of tortoise
button = 500
widthRange = 500
num = 5
t=[]
for i in range(num):
    t.append(Tortoise(i))
tIndex = 0
t[0].visible = True


while True:
#游戏主循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #接收到退出事件后退出程序
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if result == "Failed" or result =="You win~":
                x, y = pygame.mouse.get_pos()
                if x<=300 and x>=200 and y>200 and y<=300:
                    for i in range(num):
                        t[i]=Tortoise(i)
                    tIndex = 0
                    result = "playing"
                    button = 500
                    widthRange = 500
                    t[0].visible = True
            else:
                times += 1
                t[tIndex].zoomFlag = -1
                t[tIndex].moveFlag = 1
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                times += 1
                t[tIndex].zoomFlag = -1
                t[tIndex].moveFlag = 1
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((500, 500), FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode((500, 500), 0, 32)
                


    
    text1 = font.render("mouse button done: %d" % times, 1, (0, 0, 0))
    text2 = font.render("result:" +result, 1, (0, 0, 0))

    
    screen.blit(background, (0,0))

    screen.blit(text1, (0, 0))
    screen.blit(text2, (0, 20))

    if t[tIndex].zoomFlag !=-1:
        t[tIndex].zoom()

    if t[tIndex].moveFlag == 1:
        t[tIndex].move(button)
    elif t[tIndex].moveFlag == -1:
        button -= t[tIndex].height
        if widthRange <= t[tIndex].width:
            result = "Failed"
        else:
            if tIndex ==4:
                result = "You win~"
            else:
                widthRange = t[tIndex].width
                tIndex +=1
                tIndex = tIndex %5
                t[tIndex].visible = True

    for i in range(num):
        if t[i].visible == True:
            pygame.draw.rect(screen,t[i].col,t[i].rec)

    if result == "Failed" or result =="You win~":
        screen.blit(once_more,(200,200))

    
    pygame.display.update()
    #刷新一下画面
