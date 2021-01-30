import pygame
import player

from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_ESCAPE,
	KEYDOWN,
	QUIT,
)

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Swamphack VII')

player = player.Player()

gameActive = True
while gameActive:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameActive = False

	screen.fill((0, 0, 0))
	#draws player on screen
	screen.blit(player.surf, player.rect)
	#updates display
	pygame.display.flip()

pygame.quit()

