import pygame
import scripts.player as player
import scripts.wall as wall

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

player1 = player.Player()
wall1 = wall.Wall()

gameActive = True
while gameActive:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameActive = False

	screen.fill((0, 0, 0))
	#draws player on screen
	screen.blit(player1.surf, player1.rect)
	screen.blit(wall1.surf, wall1.rect)
	#updates display
	pygame.display.flip()

pygame.quit()

