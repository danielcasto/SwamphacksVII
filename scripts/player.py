import pygame

# player is child of Sprite
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		self.surf = pygame.Surface((69, 69))
		self.surf = pygame.image.load("img/Gator_right.png").convert()
		self.rect = self.surf.get_rect()

