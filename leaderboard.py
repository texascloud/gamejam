from __future__ import print_function
from operator import itemgetter
import sys, pygame, csv
from pygame.locals import *

def scores():
	pygame.display.set_caption('Snake Solver - Leaderboard')
	size = width, height = 1280, 700
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()

	font = pygame.font.SysFont('Arial', 30)
	black = 0, 0, 0
	white = 255, 255, 255

	gameExit = False
	fps = 60
	casualScoreList =[]
	hardScoreList =[]

	with open('scores.txt', 'r') as f:
		reader = csv.reader(f, delimiter=",")
		for row in reader:
			casualScoreList.append(row)

	for i in range(len(casualScoreList)):
		casualScoreList[i] = (casualScoreList[i][0], int(casualScoreList[i][1]))
	casualScoreList = sorted(casualScoreList, key=itemgetter(1))
	casualScoreList = casualScoreList[::-1]

	with open('ERECTscores.txt', 'r') as f:
		reader = csv.reader(f, delimiter=",")
		for row in reader:
			hardScoreList.append(row)

	for i in range(len(hardScoreList)):
		hardScoreList[i] = (hardScoreList[i][0], int(hardScoreList[i][1]))
	hardScoreList = sorted(hardScoreList, key=itemgetter(1))
	hardScoreList = hardScoreList[::-1]

	# f = open('scores.txt', 'w+')
	# for l in f.readlines():
	# 	print l.strip().split(", ")

	while not gameExit:
		clock.tick(fps)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
				pygame.quit()
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
		screen.blit(returnFontText, [width/2-(returnFontText_rect.w/2),height-65])
		
		#########CASUAL#########
		subTitleFont = pygame.font.SysFont('Arial', 20)
		subTitleFont.set_underline(True)
		subTitleFont.set_bold(True)
		casualText = subTitleFont.render("FUCKING CASUALS", True, black)
		casualText_rect = casualText.get_rect()
		screen.blit(casualText, [width/4-(casualText_rect.w/2)+ 29,height/8+30])

		#########HARDCORE#########
		casualText = subTitleFont.render("SO HARDCORE", True, black)
		casualText_rect = casualText.get_rect()
		screen.blit(casualText, [width-(casualText_rect.w)- 120,height/8+30])

		#########SCORES#########
		pygame.draw.line(screen, black, (width/2, height/7+5), (width/2, height-80), 4)
		scoreFont = pygame.font.SysFont('Arial', 25)
		for i in range(len(casualScoreList)):
			###NAMES###
			nameText = scoreFont.render(str(i+1) + ". " + casualScoreList[i][0], True, black)
			nameText_rect = nameText.get_rect()
			screen.blit(nameText, [width/4-75,(height/8-40)+(50*(i+2))])
			###SCORES###
			scoreText = scoreFont.render("   - - -      " + str(casualScoreList[i][1]), True, black)
			scoreText_rect = scoreText.get_rect()
			screen.blit(scoreText, [width/4+10,(height/8-40)+(50*(i+2))])

		for i in range(len(hardScoreList)):
			###NAMES###
			nameText = scoreFont.render(str(i+1) + ". " + hardScoreList[i][0], True, black)
			nameText_rect = nameText.get_rect()
			screen.blit(nameText, [((width*2)/3)-50,(height/8-40)+(50*(i+2))])
			###SCORES###
			scoreText = scoreFont.render("   - - -      " + str(hardScoreList[i][1]), True, black)
			scoreText_rect = scoreText.get_rect()
			screen.blit(scoreText, [((width*2)/3)+50,(height/8-40)+(50*(i+2))])


		pygame.display.update()

		# if gameExit:
		# 	f.close()