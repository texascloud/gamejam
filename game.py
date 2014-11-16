import sys, pygame, random
from pygame.locals import *

def main():

	pygame.display.set_caption('Snake Solver')
	size = width, height = 800, 600
	screen = pygame.display.set_mode(size)
	clock = pygame.time.Clock()
	snakeSize = 10
	x_speed = snakeSize
	y_speed = 0
	newEquation = True


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
	correct_val = 0

	def equation():
		correct_val = random.randint(-50, 50)
		op = ops[random.randint(0, len(ops)-1)]
		var = random.randint(-50, 50)
		result = eval(str(var) + " " + op + " " + str(correct_val))
		eq = str(var) + " " + str(op) + " _ " + " = " + str(result)
		return eq

	score = 0
	fps = 40
	font = pygame.font.SysFont('Arial', 30)
	#Generates random positions -- Should be list of Rects
	def position_generator(amount):
		numList = []
		
		for i in range(amount):
			applepos = pygame.Rect(  random.randint(img_size, width - img_size), random.randint(img_size + 60, height - img_size), img_size+5, img_size+5 )
			while applepos.collidelist(numList) != -1 or applepos.collidelist(snake) != -1:
				applepos = pygame.Rect(  random.randint(img_size, width), random.randint(img_size, height), img_size, img_size )
			#add code here to check if the applepos rect collides with the snake, if so generate a new one until it no longer collides
			numList.append(applepos)
		return numList

	#START GRID ITEM VARIABLES
	img_size = 20
	num_apples = 2

	rect_object_list = position_generator(num_apples) #list of Rect objects


	#END GRID ITEM VARIABLES

	scoreFont = pygame.font.SysFont('Arial', 40)
	scoreFont.set_bold

	def gameOver(): ####################################################### GAME OVER
		gameOverFont = pygame.font.SysFont('Arial', 60)
		gameOverFont.set_bold
		gameOverText = gameOverFont.render("GAME OVER", True, (255, 0, 0))
		gameOverText_rect = gameOverText.get_rect()
		screen.blit(gameOverText, (width/2 -(gameOverText_rect.w/2), height/4)) 
		
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

		exit = False
		while not exit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0)
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						exit = True
					if event.key == pygame.K_r:
						main()
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
			gameOver()
			gameExit = True
		if y_pos < 55 or y_pos > height:
			gameOver()
			gameExit = True

		screen.fill(white)
		############################# DRAW STUFF AFTER THIS LINE #####################################
		pygame.draw.line(screen, black, (0, 59), (width, 59), 3)
		for i in range(len(snake)):
			pygame.draw.rect(screen, black, snake[i], 0)
		
		for part in range(len(snake)-1):
			idx = snake[len(snake)-1].colliderect(snake[part])
			if idx != 0:
				gameOver()
				gameExit = True;



		if newEquation:
			#create list of randomly generated numbers
<<<<<<< HEAD
			random_nums = [random.randint(0, 10) for x in range(num_apples)] #[1, 5, 7, 2]
			eq = equation()

=======
			#num_apples += 1
			rect_object_list = position_generator(num_apples)
			random_nums = [random.randint(-50, 50) for x in range(num_apples)] #[1, 5, 7, 2]
			#random_nums = []
			
>>>>>>> 5465fc566d3dcf5f5a62d147581796bd5e84f766
			newEquation = False

		########### DRAW APPLES AND 1 CORRECT VALUE ##############
		for i in range(num_apples):
			font2 = pygame.font.SysFont('Arial', img_size)
			text = font2.render( str(random_nums[i]), True, red)
			screen.blit(text, rect_object_list[i])
		
		for apple in range(len(rect_object_list)):
			if snake[len(snake)-1].colliderect(rect_object_list[apple]) != 0:
				body = pygame.Rect(x_pos, y_pos, snakeSize, snakeSize)
				snake.append(body)
				newEquation = True
				#rect_object_list = position_generator(num_apples)
				score += 1
		
		scoreText = scoreFont.render("Score: " + str(score), True, (0, 100, 0))
		scoreText_rect = scoreText.get_rect()
		screen.blit(scoreText, [5,5])

		equationText = scoreFont.render(eq, True, black)
		equationText_rect = equationText.get_rect()
		screen.blit(equationText, [width/2 - (equationText_rect.w/2),5])

		pygame.display.update()
