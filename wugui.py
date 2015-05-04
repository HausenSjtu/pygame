# -*- coding: cp936 -*-

import pygame
from pygame.locals import *
#
from sys import exit
#
pygame.init()
#



class Tortoise:
    def __init__(self,num):
        self.x = 250
        self.y = 100 -10 *num
        self.zoomdx = (0.2*num+0.2)*0.5
        self.zoomdy = (0.05*num+0.05)*0.5
        #0:big   1:small   -1:end
        self.zoomFlag = 1
        #0: not start    1: moving   -1:end
        self.moveFlag = 0
        self.visible = False
        self.width = 400
        self.height = 100
        self.maxWidth = self.width
        self.maxHeight = self.height
        self.minWidth = self.maxWidth/4
        self.minHeight = self.maxHeight/4
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
        



f_score = file('scoreForWugui.txt')
scoreLines = f_score.readlines()
f_score.close()

playersInform = {}

for line in scoreLines:
    data =  line.split('\t') 
    playersInform[data[0]] = data[1:3]

print playersInform


screen = pygame.display.set_mode((500, 500), 0, 32)
#
pygame.display.set_caption("Hello, World!")
#
background = pygame.image.load('white.png').convert()
once_more = pygame.image.load("once_more.png").convert()
scoreInformPic = pygame.image.load('scoreInform.png').convert()
wYNPic = pygame.image.load('wYN.png').convert()
newGamePic = pygame.image.load('newGame.png').convert()
#

font = pygame.font.Font(None, 32)


sur = pygame.surface.Surface((200, 200))


#parameter
result="playing"
Fullscreen = False
gameStart = False

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
        	if gameStart == True:
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
	                t[tIndex].zoomFlag = -1
	                t[tIndex].moveFlag = 1
	        else:
	            x, y = pygame.mouse.get_pos()
	            if x>150 and x<350 and y>150 and y<200:
	            	# new game
	            	i=1
	            elif x>150 and x<350 and y>250 and y<300:
	            	# show the score information
	            	scoreNum = min(5,len(scoreLines))
	            	text1 = font.render("playerName\tgameNum\tscore", 1, (0, 0, 0))
            		screen.blit(text1[i], (0, 40)) 
            		i = 1
	       #      	for playerName in playersInform.keys():
	       #      		inform = playersInform[playerName]
	  					# text123= font.render('h' , 1, (0, 0, 0))
	       #      		screen.blit(text123, (0, 20+i*20))
	       #      		i += 1	


        if event.type == KEYDOWN:
        	if gameStart == True:
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
                



    
    screen.fill((255, 255, 255))

	

    
    
    pygame.display.update()
    #
