import sys, pygame
from pygame.locals import *

def instructions():
	pygame.display.set_caption('Snake Solver - Instructions')
	size = width, height = 1280, 700
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()

	font = pygame.font.SysFont('Arial', 30)
	black = 0, 0, 0
	white = 255, 255, 255

	gameExit = False
	fps = 60

	while not gameExit:
		clock.tick(fps)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
				sys.exit(0)
			elif event.type == pygame.KEYDOWN:
				gameExit = True

		screen.fill(white)

		#########TITLE#########
		titleFont = pygame.font.SysFont('Arial', 60)
		titleFont.set_underline(True)
		title = titleFont.render("Instructions", True, black)

		title_rect = title.get_rect()
		screen.blit(title, [width/2-(title_rect.w/2),height/8 - 50])

		#########PLAYER1#########
		instructionsFont = pygame.font.SysFont('Comic Sans', 40)
		player1Text = instructionsFont.render("Player 1 Controls: Arrow Keys", True, black)
		player1Text_rect = player1Text.get_rect()
		screen.blit(player1Text, [width/2-(player1Text_rect.w/2),height/4])

		#########PLAYER1#########
		player2Text = instructionsFont.render("Player 2 Controls: WASD", True, black)
		player2Text_rect = player2Text.get_rect()
		screen.blit(player2Text, [width/2-(player2Text_rect.w/2),height/4+50])

		#########SWITCHING#########
		casualText = instructionsFont.render("If you're a filthy casual, controls will switch between players every 3 equations", True, black)
		casualText_rect = casualText.get_rect()
		screen.blit(casualText, [width/2-(casualText_rect.w/2),height/4+150])

		#########SWITCHING2#########
		hardText = instructionsFont.render("On Hard Mode, controls switch after every equation", True, black)
		hardText_rect = hardText.get_rect()
		screen.blit(hardText, [width/2-(hardText_rect.w/2),height/4+200])

		#########TIME1#########
		timeText1 = instructionsFont.render("On Casual Mode, you will have 15 seconds to solve each equation", True, black)
		timeText1_rect = timeText1.get_rect()
		screen.blit(timeText1, [width/2-(timeText1_rect.w/2),height/2 + 100])

		#########TIME2#########
		timeText2 = instructionsFont.render("On Hard Mode, this decreases to 10 seconds", True, black)
		timeText2_rect = timeText2.get_rect()
		screen.blit(timeText2, [width/2-(timeText2_rect.w/2),height/2 + 150])

		#########RETURN#########
		returnFont = pygame.font.SysFont('Arial', 25)
		returnFontText = returnFont.render("Press Any Key To Return To Menu", True, black)
		returnFontText_rect = returnFontText.get_rect()
		screen.blit(returnFontText, [width/2-(returnFontText_rect.w/2),height-65])

		pygame.display.update()