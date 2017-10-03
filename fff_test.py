# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 17:39:05 2017

@author: smadvani
flicker fusion frequency test
pygame drawing from https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
"""
import pygame
import sys
import time


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))
white = (255,255,255)
black = (0,0,0)
delay = time.sleep(.001)
dely_lng = time.sleep(.1)

#x = 1
#while x<15:
screen.fill(black)
pygame.display.update()
while (True):
    msElapsed = clock.tick(1000)
    pygame.draw.circle(screen, white, (320,240), 100, 0)
    pygame.display.update()
    #dely_lng
    pygame.time.delay(100)
    pygame.draw.circle(screen, black, (320,240), 100, 0)
    pygame.display.update()
    #delay    
    pygame.time.delay(2)
    #msElapsed = clock.tick(1)
    #pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();
    #screen.fill(white)
    #x=x+1

