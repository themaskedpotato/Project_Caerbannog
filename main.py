try:
	import pygame
	import sys
	import random
	import math
	import os
	from constants import *
	from socket import *
	from pygame.locals import *
	from map_gen import *
	from room import *
except ImportError as err:
	print ("A module cannot be loaded")
	sys.exit(2)

myArrayOfChar = []
myArrayOfRoom = []

my_map_generator = map_gen_options(9,10,1,6)
my_map = map(myArrayOfRoom, my_map_generator)

room_gen = room_gen_options(10,10,1,6,"square")
room = room(myArrayOfChar, room_gen)


pygame.init()
screen_size = [SCREEN_WIDTH, SCREEN_HEIGHT]
fenetre = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Project Caerbannog")
fenetre.fill(WHITE)

# Affichage d'un texte
font = pygame.font.Font(None, 36)
text = font.render("Project Caerbannog", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = fenetre.get_rect().centerx
textpos.centery = fenetre.get_rect().centery
fenetre.blit(text, textpos)
pygame.display.flip()

continuer = 1

#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
