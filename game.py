import sys, pygame, random, csv, eztext, string
from operator import itemgetter
from pygame.locals import *

def main(hardMode, startTime):
	pygame.display.set_caption('Snake Solver')
	size = width, height = 1280, 700
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()
	snakeSize = 10
	x_speed = snakeSize
	y_speed = 0
	newEquation = True
	turns = 3
	if hardMode: turns = 1
	player2 = False
	black = 0, 0, 0
	white = 255, 255, 255
	red = 255, 0, 0
	blue = 0, 0, 255
	snake_color = black

	font = pygame.font.SysFont('Arial', 30)
	gameExit = False
	x_pos = 300
	y_pos = 300
	snake = [pygame.Rect(x_pos, y_pos, snakeSize, snakeSize)]

	numRange = 49
	ops = ["+", "-"]
	eq = ""
	solved_eq = ""
	correct_val = 0
	#real_rect = pygame.Rect(  random.randint(img_size, width - img_size), random.randint(img_size + 60, height - img_size), img_size+5, img_size+5 )

	def equation():
		correct_val = random.randint(-20, 20)
		op = ops[random.randint(0, len(ops)-1)]
		var = random.randint(-numRange, numRange)
		result = eval(str(var) + " " + op + " " + str(correct_val))
		eq = str(var) + " " + str(op) + " _ " + " = " + str(result)
		solved_eq = str(var) + " " +str(op) + " "+ str(correct_val) + " = " + str(result)
		return (eq, correct_val, solved_eq)

	score = 0
	fps = 20
	font = pygame.font.SysFont('Arial', 30)
	############################################################# Generates random positions -- Should be list of Rects
	def position_generator(amount, snake_head = None):
		if snake_head is None: snake_head = pygame.Rect(0,0,0,0)
		numList = []
		for i in range(amount):
			applepos = pygame.Rect(  random.randint(img_size, width - img_size), random.randint(img_size + 50, height - img_size), img_size+10, img_size+10 )
			#check if the applepos rect collides with the snake, if so generate a new one until it no longer collides
			while applepos.collidelist(numList) != -1 and applepos.collidelist(snake) != -1:
				applepos = pygame.Rect(  random.randint(img_size, width - img_size), random.randint(img_size + 50, height - img_size), img_size+10, img_size+10 )
			numList.append(applepos)
		return numList

	#START GRID ITEM VARIABLES
	img_size = 20
	num_apples = 7
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
			pygame.display.update()
			pygame.draw.rect(screen, white, pygame.Rect(0, height/4+40, width, 50), 0)
			promptText = scoreFont.render("Enter Name: " + string.join(name,""), True, black)
			promptText_rect = promptText.get_rect()
			screen.blit(promptText, [width/2 - (promptText_rect.w/2),height/4 + 40])
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					nameEntered = True
					pygame.quit()
					sys.exit(0)
				else:
					inkey = get_key()
					if inkey == K_BACKSPACE:
						name = name[0:-1]
					elif inkey == K_RETURN:
						nameEntered = True
					elif inkey <= 127:
						if len(name) < 6:
							name.append(chr(inkey))


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
		if hardMode: scoreFile = 'ERECTscores.txt'
		else: scoreFile = 'scores.txt'
		with open(scoreFile, 'r') as f:
			reader = csv.reader(f, delimiter=",")
			for row in reader:
				leaderboardList.append(row)
		
		for i in range(len(leaderboardList)):
			leaderboardList[i] = (leaderboardList[i][0], int(leaderboardList[i][1]))
		
		scores = sorted(leaderboardList, key=itemgetter(1))
		if end_score > scores[0][1]:
			name = getName()
			scores[0] = (name, end_score)

		with open(scoreFile, "w") as f:
		    csv.register_dialect("custom", delimiter=",", skipinitialspace=True)
		    writer = csv.writer(f, dialect="custom")
		    for tup in scores:
        		writer.writerow(tup)

		pygame.display.update()

		exit = False
		while not exit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit = True
					pygame.quit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						exit = True
					if event.key == pygame.K_r:
						t = pygame.time.get_ticks()
						main(hardMode, t)
						exit = True
	
	while not gameExit:
		currentTime = (pygame.time.get_ticks() / 1000.0) - (startTime / 1000.0)
		if hardMode:
			if currentTime > 10.0:
				gameOver(score)
				gameExit = True
		else:
			if currentTime > 15.0:
				gameOver(score)
				gameExit = True


		clock.tick(fps)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					gameExit = True
					pygame.quit()
			elif not player2:
				if event.type == pygame.KEYDOWN:
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
			else:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_a and x_speed == 0:
						x_speed = -snakeSize
						y_speed = 0
					if event.key == pygame.K_d and x_speed == 0:
						x_speed = snakeSize
						y_speed = 0
					if event.key == pygame.K_w and y_speed == 0:
						x_speed = 0
						y_speed = -snakeSize
					if event.key == pygame.K_s and y_speed == 0:
						x_speed = 0
						y_speed = snakeSize

		x_pos += x_speed
		y_pos += y_speed

		for i in range(len(snake)-1):
			snake[i] = snake[i+1]

		
		snake[len(snake)-1] = pygame.Rect(x_pos, y_pos, snakeSize, snakeSize)
		snake_head_collider = pygame.Rect(x_pos, y_pos, snakeSize + 50, snakeSize + 50)

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
			pygame.draw.rect(screen, snake_color, snake[i], 0)
		
		for part in range(len(snake)-1):
			idx = snake[len(snake)-1].colliderect(snake[part])
			if idx != 0:
				gameOver(score)
				gameExit = True;



		if newEquation:
			#create list of randomly generated numbers
			eq, correct_val, solved_eq = equation()
			startTime =  pygame.time.get_ticks()
			if hardMode: fps += 5
			else: fps += 2
			if hardMode:
				num_apples += 2
				numRange = 7*num_apples
			if num_apples > 14: ops.append("*")
			rect_object_list = position_generator(num_apples, snake_head_collider)
			random_nums = []
			for x in range(num_apples):
				rndm = random.randint(-20, 20)
				while (rndm == correct_val) or (rndm in random_nums):
					rndm = random.randint(-20, 20)
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

					if score % turns == 0:
						player2 = not player2
						if snake_color is blue:
							snake_color = black
						else:
							snake_color = blue
				else:
					gameOver(score)
					gameExit= True
		
		#######SCORE#######			
		scoreText = scoreFont.render("Score: " + str(score), True, (0, 100, 0))
		scoreText_rect = scoreText.get_rect()
		screen.blit(scoreText, [5,5])

		#######EQUATION#######	
		equationText = scoreFont.render(eq, True, black)
		equationText_rect = equationText.get_rect()
		screen.blit(equationText, [width/2 - (equationText_rect.w/2),5])

		#######TIME#######	
		timeText = scoreFont.render(str(currentTime), True, (0, 100, 0))
		timeText_rect = timeText.get_rect()
		screen.blit(timeText, [(width*7)/8,5])

		pygame.display.update()
