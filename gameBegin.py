
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)

pygame.display.set_caption("Hello, World!")


# load pictures
scoreInformPic = pygame.image.load('scoreInform.png').convert()
wYNPic = pygame.image.load('wYN.png').convert()
newGamePic = pygame.image.load('newGame.png').convert()
goBackPic = pygame.image.load('goBack.png').convert()

# load players information
f_score = file('scoreForWugui.txt')
scoreLines = f_score.readlines()
f_score.close()
playersInform = {}
for line in scoreLines:
    data =  line.split('\t')
    playersInform[data[0]] = [data[1],data[2].strip('\n')]


# initial some varibles
scoreInformRect = Rect(150,250,200,50)
goBackRect = Rect((150,400),(200,50))
newGameRect = Rect(150,150,200,50)
font = pygame.font.Font(None, 32)
showModes = {'menuStart', 'menuScore', 'gaming','menuEnd'}
mode = 'menuScore'

while True:
    screen.fill((255,255,255))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if mode == 'menuStart':
                if scoreInformRect.collidepoint((x,y))==True:
                    mode = 'menuScore'
                if newGameRect.collidepoint((x,y))==True:
                    mode = 'gaming'
            elif mode == 'menuScore':
                if goBackRect.collidepoint((x,y))==True:
                    mode = 'menuStart'

    if mode == 'menuStart':        
        screen.blit(newGamePic,newGameRect[0:2])
        screen.blit(scoreInformPic,scoreInformRect[0:2])
    elif mode == 'menuScore':
        text1 = font.render("Name", 1, (0, 0, 0))
        screen.blit(text1, (75,50))
        text1 = font.render("Count", 1, (0, 0, 0))
        screen.blit(text1, (200,50))
        text1 = font.render("Score", 1, (0, 0, 0))
        screen.blit(text1, (320,50))
        i = 1
        for playerName in playersInform:
            playerInform = playersInform[playerName]
            text1 = font.render(playerName, 1, (0, 0, 0))
            screen.blit(text1, (75,50+i*50))
            text1 = font.render(playerInform[0], 1, (0, 0, 0))
            screen.blit(text1, (200,50+i*50))
            text1 = font.render(playerInform[1], 1, (0, 0, 0))
            screen.blit(text1, (320,50+i*50))
            i += 1
        screen.blit(goBackPic,goBackRect[0:2])
    elif mode == 'gaming':
        pass
        
        
    pygame.display.update()
