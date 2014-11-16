import sys, pygame
from pygame.locals import *

def scores():
	pygame.display.set_caption('Snake Solver - Leaderboard')
	size = width, height = 800, 600
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()

	font = pygame.font.SysFont('Arial', 30)
	black = 0, 0, 0
	white = 255, 255, 255

	gameExit = False
	fps = 120

	while not gameExit:
		clock.tick(fps)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			elif event.type == pygame.KEYDOWN:
				gameExit = True

		screen.fill(white)

		#########TITLE#########
		titleFont = pygame.font.SysFont('Arial', 60)
		titleFont.set_underline(True)
		title = titleFont.render("Leaderboard", True, black)
		title_rect = title.get_rect()
		screen.blit(title, [width/2-(title_rect.w/2),height/8 - 50])

		#########RETURN#########
		returnFont = pygame.font.SysFont('Arial', 25)
		returnFontText = returnFont.render("Press Any Key To Return To Menu", True, black)
		returnFontText_rect = returnFontText.get_rect()
		screen.blit(returnFontText, [width/2-(returnFontText_rect.w/2),height-100])

		pygame.display.update()