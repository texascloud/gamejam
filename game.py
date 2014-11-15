import sys, pygame, random
from pygame.locals import *
def main():
	pygame.init()

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
	for x in range(20):
		body = pygame.Rect(x_pos, y_pos, snakeSize, snakeSize)
		snake.append(body)

	fps = 40
	font = pygame.font.SysFont('Arial', 30)

	#Generates random positions -- Should be list of Rects
	def position_generator(amount):
		numList = []
		
		for i in range(amount):
			applepos = pygame.Rect(  random.randint(img_size, 590), random.randint(img_size, 590), snakeSize, snakeSize )
			#add code here to check if the applepos rect collides with the snake, if so generate a new one until it no longer collides
			numList.append(applepos)
		return numList

	#START GRID ITEM VARIABLES
	img_size = 20
	num_apples = 4
	rect_object_list = position_generator(num_apples) #list of 
	#applepos = pygame.Rect(  random.randint(0, 590), random.randint(0, 590), snakeSize, snakeSize )
	appleimage = pygame.Surface((10, 10))
	appleimage.fill((0, 255, 0))
	#END GRID ITEM VARIABLES

	def gameOver(s): ####################################################### GAME OVER
		text = font.render("GAME OVER", True, (255, 0, 0))
		text_rect = text.get_rect()
		screen.blit(text, (width/2 -(text_rect.w/2), height/2)) 
		pygame.display.update()
		pygame.time.wait(2000)

		# if s == "self":
		# 	print "STOP TOUCHING YOURSELF!"
		# elif s == "wall":
		# 	print "DON'T TOUCH THAT!"

	while not gameExit:
		clock.tick(fps)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
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
			gameOver("wall")
			gameExit = True
		if y_pos < 0 or y_pos > height:
			gameOver("wall")
			gameExit = True

		screen.fill(white)
		#############################DRAW STUFF AFTER THIS LINE #####################################
		for i in range(len(snake)):
			pygame.draw.rect(screen, black, snake[i], 0)
		
		for part in range(len(snake)-1):
			idx = snake[len(snake)-1].colliderect(snake[part])
			if idx != 0:
				gameOver("self")
				gameExit = True;



		if newEquation:
			#create list of randomly generated numbers
			random_nums = [random.randint(0, 10) for x in range(num_apples)] #[1, 5, 7, 2]
			newEquation = False

		for i in range(num_apples):
			font2 = pygame.font.SysFont('Arial', img_size)
			text = font2.render( str(random_nums[i]), True, red)
			screen.blit(text, rect_object_list[i])
		
			 
		# idx = head.collidelist(snake)
		# if(idx < 0):
		# 	print idx

		pygame.display.update()
