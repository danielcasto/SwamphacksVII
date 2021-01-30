# player is child of Sprite
import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		# TODO
		self.surf = pygame.Surface((100, 100))
		self.surf = pygame.image.load("img/wall_segment.png").convert()
		
		self.rect = self.surf.get_rect()
