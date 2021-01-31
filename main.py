import pygame
import scripts.player as player
import scripts.wall_seg as wall
import scripts.bank as bank
from pygame import mixer

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

pygame.mixer.music.load('songs/ElectronicFantasy.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Swamphack VII')

player1 = player.Player()
wall1 = wall.Wall()

surface = pygame.image.load("img/Screen.png")

atmSurface = pygame.image.load("img/ATM.jpg")
atmRect = atmSurface.get_rect()

text = ''


##### main maze and atm stuff below
maze = True
atm = True
while maze:
	for event in pygame.event.get():
		if event.type == KEYDOWN:

			# If the Esc key is pressed, then exit the main loop
			if event.key == K_ESCAPE:
				maze = False
				atm = False

			if event.key == K_RIGHT:
				maze = False

		if event.type == pygame.QUIT:
			maze = False
			atm = False

	player1.update(pygame.key.get_pressed(), SCREEN_WIDTH, SCREEN_HEIGHT)
	wall1.update(pygame.key.get_pressed(), SCREEN_WIDTH, SCREEN_HEIGHT)

	screen.fill((255, 127, 39))
	screen.blit(wall1.surf, wall1.rect)
	screen.blit(player1.surf, player1.rect)
	#updates display
	pygame.display.flip()


font = pygame.font.Font('freesansbold.ttf', 32)
userInfo = ["Email Address", "Password"]
bankInfo = bank.BankAccount('Email Address', 'Password')
i = 0
userTyped = False
infoEntered = False
while atm:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			# If the Esc key is pressed, then exit the main loop
			if event.key == K_ESCAPE:
				atm = False
			elif event.key == pygame.K_RETURN:
				if i == 0:
					bankInfo.email_address = text
				elif i == 1:
					bankInfo.Password = text

				text = ''
				userTyped = False
				i = i + 1

				if i >= 2:
					infoEntered = True
			elif event.key == pygame.K_BACKSPACE:
				text = text[:-1]
			else:
				if not userTyped:
					userTyped = True
					text = ''

				text += event.unicode

		if event.type == pygame.QUIT:
			atm = False

	if not userTyped and not infoEntered:
		text  = userInfo[i]

	if infoEntered:
		text = 'Balance: $' + str(bankInfo.GetBalance()) 

	displayText = font.render(text, True, green, blue)
	displayTextRect = displayText.get_rect()
	displayTextRect.center = (450, 180)
	#TODO figure out typing
	screen.fill((0, 0, 0))
	screen.blit(atmSurface, atmRect)
	screen.blit(displayText, displayTextRect)

	#updates display
	pygame.display.flip()



pygame.quit()
