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
	from room_gen import *
except ImportError as err:
	print ("A module cannot be loaded")
	sys.exit(2)

array_of_char = []
array_of_room = []

room_genenerator = room_gen_options(10,10,1,6,"square")
room = room(array_of_char, room_genenerator)

map_generator = map_gen_options(9,10,1,6)
my_map = map(array_of_room, map_generator)

array_of_char = get_RoundRoom(10, 25) #pos x
array_of_char = floor_filling(ra)
screen_size = get_room_size(array_of_char)


# Create the window
pygame.init()
fenetre = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Project Caerbannog")
fenetre.fill(WHITE)

# Tiles textures
WALL_TEXTURE = pygame.image.load("wall.png").convert()
FLOOR_TEXTURE = pygame.image.load("floor.png").convert()
VOID_TEXTURE = pygame.image.load("void.png").convert()

for i in range(len(array_of_char)):
    for j in range(len(array_of_char[i])):
        if array_of_char[i][j] == WALL:
            fenetre.blit(WALL_TEXTURE, (i*32, j*32))
            pygame.display.flip()
        elif array_of_char[i][j] == FLOOR:
            fenetre.blit(FLOOR_TEXTURE, (i*32, j*32))
            pygame.display.flip()
        elif array_of_char[i][j] == VOID:
            fenetre.blit(VOID_TEXTURE, (i*32, j*32))
            pygame.display.flip()

#Boucle infinie
continuer = 1
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
