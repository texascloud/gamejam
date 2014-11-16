import sys, pygame, random, csv, eztext, string
from operator import itemgetter
from pygame.locals import *

def main(hardMode):

	pygame.display.set_caption('Snake Solver')
	size = width, height = 800, 600
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()
	snakeSize = 10
	x_speed = snakeSize
	y_speed = 0
	newEquation = True
	txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='type here: ')


	black = 0, 0, 0
	white = 255, 255, 255
	red = 255, 0, 0

	font = pygame.font.SysFont('Arial', 30)
	gameExit = False
	x_pos = 300
	y_pos = 300
	snake = [pygame.Rect(x_pos, y_pos, snakeSize, snakeSize)]

	ops = ["+", "-"]
	eq = ""
	solved_eq = ""
	correct_val = 0
	#real_rect = pygame.Rect(  random.randint(img_size, width - img_size), random.randint(img_size + 60, height - img_size), img_size+5, img_size+5 )

	def equation():
		correct_val = random.randint(-50, 50)
		op = ops[random.randint(0, len(ops)-1)]
		var = random.randint(-50, 50)
		result = eval(str(var) + " " + op + " " + str(correct_val))
		eq = str(var) + " " + str(op) + " _ " + " = " + str(result)
		solved_eq = str(var) +str(op) + " "+ str(correct_val) + " = " + str(result)
		return (eq, correct_val, solved_eq)

	score = 0
	fps = 20
	font = pygame.font.SysFont('Arial', 30)
	############################################################# Generates random positions -- Should be list of Rects
	def position_generator(amount):
		numList = []
		for i in range(amount):
			applepos = pygame.Rect(  random.randint(img_size, width - (img_size+10)), random.randint(img_size + 50, height - img_size), img_size+10, img_size+10 )
			#check if the applepos rect collides with the snake, if so generate a new one until it no longer collides
			while applepos.collidelist(numList) != -1 or applepos.collidelist(snake) != -1:
				applepos = pygame.Rect(  random.randint(img_size, width), random.randint(img_size, height), img_size, img_size )
			numList.append(applepos)
		return numList

	#START GRID ITEM VARIABLES
	img_size = 20
	num_apples = 6
	rect_object_list = position_generator(num_apples) #list of Rect objects
	#END GRID ITEM VARIABLES

	scoreFont = pygame.font.SysFont('Arial', 40)
	scoreFont.set_bold

	def get_key():
		while 1:
			event = pygame.event.poll()
			if event.type == KEYDOWN:
				return event.key
			else:
				pass

	def getName():
		nameEntered = False
		name = []

		while not nameEntered:
			promptText = scoreFont.render("Enter Name: " + string.join(name,""), True, black)
			promptText_rect = promptText.get_rect()
			screen.blit(promptText, [width/2 - (promptText_rect.w/2),height/4 + 10])
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
				else:
					inkey = get_key()
					if inkey == K_BACKSPACE:
						name = name[0:-1]
					elif inkey == K_RETURN:
						nameEntered = True
					elif inkey <= 127:
						name.append(chr(inkey))



				# elif event.type == K_BACKSPACE:
			 #    	name = name[0:-1]
			 #    elif event.type == K_RETURN:
			 #    	break
			 #    else
			 #    	if len(name) < 10:
				#     	name.append(chr(inkey))

			promptText = scoreFont.render("Enter Name: " + string.join(name,""), True, black)
			promptText_rect = promptText.get_rect()
			screen.blit(promptText, [width/2 - (promptText_rect.w/2),height/4 + 10])
		return string.join(name,"")

	def gameOver(end_score): ####################################################### GAME OVER ###########
		screen.fill(white) #necessary

		solvedEquationText = scoreFont.render(solved_eq, True, black)
		solvedEquationText_rect = solvedEquationText.get_rect()
		screen.blit(solvedEquationText, [width/2 - (solvedEquationText_rect.w/2),5])

		gameOverFont = pygame.font.SysFont('Arial', 60)
		gameOverFont.set_bold
		gameOverText = gameOverFont.render("GAME OVER", True, (255, 0, 0))
		gameOverText_rect = gameOverText.get_rect()
		screen.blit(gameOverText, (width/2 -(gameOverText_rect.w/2), height/4 - 30)) 
		
		scoreText = scoreFont.render("Score: " + str(score), True, (0, 100, 0))
		scoreText_rect = scoreText.get_rect()
		screen.blit(scoreText, [5,5])
		
		returnFont = pygame.font.SysFont('Arial', 30)
		returnText = returnFont.render("Press 'Enter' to Return To Menu", True, (0, 0, 255))
		return_rect = returnText.get_rect()
		screen.blit(returnText, [width/2-(return_rect.w/2),height/2])

		retryText = returnFont.render("Press 'R' to Play Again", True, (0, 0, 255))
		retryText_rect = retryText.get_rect()
		screen.blit(retryText, [width/2-(retryText_rect.w/2),height/2 - 50])

		pygame.display.update()

		leaderboardList = []
		with open('scores.txt', 'r') as f:
			reader = csv.reader(f, delimiter=",")
			for row in reader:
				leaderboardList.append(row)
		
		for i in range(len(leaderboardList)):
			leaderboardList[i] = (leaderboardList[i][0], int(leaderboardList[i][1]))
		
		scores = sorted(leaderboardList, key=itemgetter(1))
		if end_score > scores[0][1]:
			# name = inputbox.ask(screen, "Enter Name")
			name = getName()
			scores[0] = (name, end_score)

		with open("scores.txt", "w") as f:
		    csv.register_dialect("custom", delimiter=",", skipinitialspace=True)
		    writer = csv.writer(f, dialect="custom")
		    for tup in scores:
        		writer.writerow(tup)

		pygame.display.update()

		exit = False
		while not exit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						exit = True
					if event.key == pygame.K_r:
						main(hardMode)
						exit = True
	
	while not gameExit:
		clock.tick(fps)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit(0)
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and x_speed == 0:
					x_speed = -snakeSize
					y_speed = 0
				if event.key == pygame.K_RIGHT and x_speed == 0:
					x_speed = snakeSize
					y_speed = 0
				if event.key == pygame.K_UP and y_speed == 0:
					x_speed = 0
					y_speed = -snakeSize
				if event.key == pygame.K_DOWN and y_speed == 0:
					x_speed = 0
					y_speed = snakeSize

		x_pos += x_speed
		y_pos += y_speed

		for i in range(len(snake)-1):
			snake[i] = snake[i+1]

		
		snake[len(snake)-1] = pygame.Rect(x_pos, y_pos, snakeSize, snakeSize)

		if x_pos < 0 or x_pos > width:
			gameOver(score)
			gameExit = True
		if y_pos < 55 or y_pos > height:
			gameOver(score)
			gameExit = True

		screen.fill(white)
		############################# DRAW STUFF AFTER THIS LINE #####################################
		pygame.draw.line(screen, black, (0, 59), (width, 59), 3)
		for i in range(len(snake)):
			pygame.draw.rect(screen, black, snake[i], 0)
		
		for part in range(len(snake)-1):
			idx = snake[len(snake)-1].colliderect(snake[part])
			if idx != 0:
				gameOver(score)
				gameExit = True;



		if newEquation:
			#create list of randomly generated numbers
			eq, correct_val, solved_eq = equation()
			fps += 2
			if hardMode:
				num_apples += 1 
			rect_object_list = position_generator(num_apples)
			#random_nums = [random.randint(-50, 50) for x in range(num_apples)] #[1, 5, 7, 2]
			random_nums = []
			for x in range(num_apples):
				rndm = random.randint(-50, 50)
				while rndm is correct_val:
					rndm = random.randint(-50, 50)
				random_nums.append(rndm)
			newEquation = False

		########### DRAW APPLES AND 1 CORRECT VALUE ##############
		rect_font = pygame.font.SysFont('Arial', img_size)
		text = rect_font.render( str(correct_val), True, red)
		screen.blit(text, rect_object_list[0])
		for i in range(1,num_apples):
			text = rect_font.render( str(random_nums[i]), True, red)
			screen.blit(text, rect_object_list[i])
		
		
		for apple in range(len(rect_object_list)):
			if snake[len(snake)-1].colliderect(rect_object_list[apple]) != 0:
				if apple == 0:
					#print 'CORRECT VALUE BISH' 
					body = pygame.Rect(x_pos, y_pos, snakeSize, snakeSize)
					snake.append(body)
					newEquation = True
					#rect_object_list = position_generator(num_apples)
					score += 1
				else:
					gameOver(score)
					gameExit= True
		
		scoreText = scoreFont.render("Score: " + str(score), True, (0, 100, 0))
		scoreText_rect = scoreText.get_rect()
		screen.blit(scoreText, [5,5])

		equationText = scoreFont.render(eq, True, black)
		equationText_rect = equationText.get_rect()
		screen.blit(equationText, [width/2 - (equationText_rect.w/2),5])

		pygame.display.update()
