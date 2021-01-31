import pygame

from pygame.locals import (
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_ESCAPE,
	KEYDOWN,
	QUIT,
)



# player is child of Sprite
class Wall(pygame.sprite.Sprite):
	def __init__(self):
		super(Wall, self).__init__()
		self.surf = pygame.Surface((3000, 750))
		self.surf = pygame.image.load("img/Screen.png").convert()
		self.rect = self.surf.get_rect()
	def update(self, pressed_keys, SCREEN_WIDTH, SCREEN_HEIGHT):
		if pressed_keys[K_LEFT]:
			self.rect.move_ip(1, 0)
			
		if pressed_keys[K_RIGHT]:
			self.rect.move_ip(-1, 0)
			
		if self.rect.left > 450:
			self.rect.left = 450
		if self.rect.right < 500:
			self.rect.right = 500
