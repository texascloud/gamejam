import sys, pygame
from pygame.locals import *
from game import main
pygame.init()

pygame.display.set_caption('Snake Solver')
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 30)
black = 0, 0, 0
white = 255, 255, 255

gameExit = False
fps = 120
pygame.mixer.music.load('cooks.mp3')
pygame.mixer.music.play()

while not gameExit:
	clock.tick(fps)

	#########TITLE#########
	titleFont = pygame.font.SysFont('Arial', 60)
	titleFont.set_bold
	title = titleFont.render("Snake Solver", True, black)
	title_rect = title.get_rect()

	#########SUB-TITLE#########
	subTitleFont = pygame.font.SysFont('Arial', 20)
	subTitle = subTitleFont.render("(get_rect)", True, black)
	sub_title_rect = subTitle.get_rect()

	#########START#########
	startFont = pygame.font.SysFont('Arial', 45)
	start = startFont.render("Press 'Enter' to Play", True, (0, 0, 255))
	start_rect = start.get_rect()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				main()

	screen.fill(white)
	screen.blit(title, [width/2-(title_rect.w/2),height/4])
	screen.blit(subTitle, [width/2-(sub_title_rect.w/2),height/3+ 15])
	screen.blit(start, [width/2-(start_rect.w/2),height/2])

	pygame.display.update()
