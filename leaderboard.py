from __future__ import print_function
import sys, pygame, csv
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
	highScoreList =[]

	with open('scores.txt', 'r') as f:
		reader = csv.reader(f, delimiter=",")
		for row in reader:
			highScoreList.append(row)

	# f = open('scores.txt', 'w+')
	# for l in f.readlines():
	# 	print l.strip().split(", ")

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

		scoreFont = pygame.font.SysFont('Arial', 25)
		for i in range(len(highScoreList)):
			nameText = scoreFont.render(str(i+1) + ". " + highScoreList[i][0], True, black)
			nameText_rect = nameText.get_rect()
			screen.blit(nameText, [width/3+20,(height/8-50)+(50*(i+2))])

			scoreText = scoreFont.render("   - - -      " + highScoreList[i][1], True, black)
			scoreText_rect = scoreText.get_rect()
			screen.blit(scoreText, [width/3+120,(height/8-50)+(50*(i+2))])


		pygame.display.update()

		# if gameExit:
		# 	f.close()