import sys, pygame, PodSixNet
from pygame.locals import *
from game import main
from leaderboard import scores
pygame.init()

pygame.display.set_caption('Snake Solver')
size = width, height = 1280, 700
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
	pygame.display.set_caption('Snake Solver')

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

	#########HARD#########
	hard = startFont.render("Press 'C' to Play Hard Mode", True, (0, 0, 255))
	hard_rect = hard.get_rect()

	#########LEADERBOARD#########
	leaderboardText = startFont.render("Press 'L' to View High Scores", True, (255, 0, 0))
	leaderboardText_rect = leaderboardText.get_rect()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				main(False, pygame.time.get_ticks() / 1000.0)
			if event.key == pygame.K_c:
				main(True, pygame.time.get_ticks() / 1000.0)
			if event.key == pygame.K_l:
				scores()

	screen.fill(white)
	screen.blit(title, [width/2-(title_rect.w/2),height/4 - 50])
	screen.blit(subTitle, [width/2-(sub_title_rect.w/2),height/4 + 15])
	screen.blit(start, [width/2-(start_rect.w/2),height/2 - 20])
	screen.blit(hard, [width/2-(hard_rect.w/2),height/2+40])
	screen.blit(leaderboardText, [width/2-(leaderboardText_rect.w/2),height/2+130])

	pygame.display.update()
