# player is child of Sprite
import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		self.surf = pygame.Surface((75, 25))
		self.surf = pygame.image.load("img/wall_segment.png").convert()
		self.surf.set_colorKey((255, 255, 255), RLEACCEL)
		self.rect = self.surf.get_rect()
