import pygame

# wall is a child of sprite
class Wall(pygame.sprite.Sprite):
	def __init__(self):
		super(Wall, self).__init__()
		self.surf = pygame.Surface((36, 32))
		self.surf = pygame.image.load("img/wall_segment.png").convert()
		self.rect = self.surf.get_rect()