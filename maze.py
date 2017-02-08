import sys; sys.path.append('..') 
import pygame
import open_bci_v3 as bci
import os
import logging
import time
from pygame.locals import *
import numpy
from collections import *
import math
import pandas as pd
import brain

pygame.init()

display_width = 800
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Maze Game by SSVEP')

white = (255,255,255)

exit = False
playerImg = pygame.image.load('player.bmp')
blockImg = pygame.image.load('block.bmp')

def player(x,y):
	gameDisplay.blit(playerImg, (x,y))

x = 250
y = 90
x_change = 0

def maze():
	M = 10
	N = 9
	maze = [ 1,1,1,1,1,1,1,1,1,1,
			 1,0,0,0,0,0,0,0,0,1,
			 1,1,1,1,1,1,1,1,0,1,
			 1,0,0,0,0,0,0,1,0,1,
			 1,0,1,1,1,1,0,1,0,1,
			 1,0,1,0,0,0,0,1,0,1,
			 1,0,1,1,1,1,1,1,0,1,
			 1,0,0,0,0,0,0,0,0,1,
			 1,1,1,1,1,1,1,1,1,1 ]
	bx = 0
	by = 0
	for i in range(0, M * N):
		if maze[ bx + (by * M) ] == 1:
			gameDisplay.blit(blockImg,( 200 + bx * 40 , 40 + by * 40 ))
		bx = bx + 1
		if bx == M:
			bx = 0 
			by = by + 1

while not exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True
		
	if brain.headto() == 'right':
		x_change = 20
	elif brain.headto() == 'left':
		x_change = -20
	elif brain.headto() == 'stay':
		x_change = 0

	x += x_change
  	
	gameDisplay.fill(white)
	player(x,y)
	maze()
		
	pygame.display.update()

pygame.quit()
quit()