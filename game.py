# -*- coding: cp936 -*-

import pygame
from sys import exit
from pygame.locals import *


#��ʼ��pygame,Ϊʹ��Ӳ����׼��
pygame.init()
#������һ������,���ڴ�С�ͱ���ͼƬ��Сһ��
screen = pygame.display.set_mode((666, 500), 0, 32) 
#���ô��ڱ���
pygame.display.set_caption("Hello, World!")
#���ز�ת��ͼ��
background1 = pygame.image.load('py1.png').convert()
background2 = pygame.image.load('py2.png').convert()
pic=1
background = background1

#����ȫ��
Fullscreen = False


#��Ϸ��ѭ��
while True:
       for event in pygame.event.get():
              #���յ��˳��¼����˳�����
              if event.type == pygame.QUIT:
                     pygame.quit()
                     exit()
              #������갴�µ��¼�
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
                            
                     
              
                     
       #������ͼ����ȥ
       screen.blit(background, (0,0))
       
       #ˢ��һ�»���
       pygame.display.update()






