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
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		self.surf = pygame.Surface((69, 69))
		self.surf = pygame.image.load("img/gator_right.png").convert()
		self.rect = self.surf.get_rect()

	def update(self, pressed_keys, SCREEN_WIDTH, SCREEN_HEIGHT):
	    if pressed_keys[K_UP]:
	        self.rect.move_ip(0, -1)
	    if pressed_keys[K_DOWN]:
	        self.rect.move_ip(0, 1)
	    if pressed_keys[K_LEFT]:
	        self.rect.move_ip(-1, 0)
	        self.surf = pygame.image.load("img/gator_left.png").convert()
	    if pressed_keys[K_RIGHT]:
	        self.rect.move_ip(1, 0)
	        self.surf = pygame.image.load("img/gator_right.png").convert()

	    # Keep player on the screen
	    if self.rect.left < 0:
	        self.rect.left = 0
	    if self.rect.right > SCREEN_WIDTH:
	        self.rect.right = SCREEN_WIDTH
	    if self.rect.top <= 0:
	        self.rect.top = 0
	    if self.rect.bottom >= SCREEN_HEIGHT:
	        self.rect.bottom = SCREEN_HEIGHT

