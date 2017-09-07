import pygame
from pygame.locals import *
from map_gen import *
from room import *

myArrayOfChar = []
myArrayOfRoom = []

my_map_generator = map_gen_options(9,10,1,6)
my_map = map(myArrayOfRoom, my_map_generator)

room_gen = room_gen_options(10,10,1,6,"square")
room = room(myArrayOfChar, room_gen)


pygame.init()
fenetre = pygame.display.set_mode((500, 500))
fenetre.fill((250, 250, 250))

# Affichage d'un texte
font = pygame.font.Font(None, 36)
text = font.render("Project Caerbannog", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = fenetre.get_rect().centerx
textpos.centery = fenetre.get_rect().centery
fenetre.blit(text, textpos)
# Blitter le tout dans la fenêtre
fenetre.blit(fenetre, (0, 0))
pygame.display.flip()

continuer = 1

#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
