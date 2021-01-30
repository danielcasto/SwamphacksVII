import pygame
import scripts.player as player
import scripts.wall_seg as wall

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
		if event.type == KEYDOWN:
			# If the Esc key is pressed, then exit the main loop
			if event.key == K_ESCAPE:
				gameActive = False

		if event.type == pygame.QUIT:
			gameActive = False

	player1.update(pygame.key.get_pressed(), SCREEN_WIDTH, SCREEN_HEIGHT)

	screen.fill((0, 0, 0))
	screen.blit(player1.surf, player1.rect)
	screen.blit(wall1.surf, wall1.rect)
	#updates display
	pygame.display.flip()

pygame.quit()

