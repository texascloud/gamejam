import sys, pygame, random
from pygame.locals import *
pygame.init()

#Generates random positions
def position_generator(amount):
	numList = []
	for i in range(amount):
		applepos = (random.randint(0, 590), random.randint(0, 590))
		numList.append(applepos)
	return numList

pygame.display.set_caption('Snake Solver')
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
snakeSize = 10
x_speed = snakeSize
y_speed = 0

#START GRID ITEM VARIABLES
num_apples = 9
num_pos = position_generator(num_apples)
appleimage = pygame.Surface((10, 10))
appleimage.fill((0, 255, 0))
#END GRID ITEM VARIABLES

black = 0, 0, 0
white = 255, 255, 255

gameExit = False
x_pos = 300
y_pos = 300
snake = [pygame.Rect(x_pos, y_pos, snakeSize, snakeSize)]
for x in range(20):
	body = pygame.Rect(0, 0, snakeSize, snakeSize)
	snake.append(body)

fps = 40

def gameOver(s):
	font = pygame.font.SysFont('Arial', 30)
	text = font.render("GAME OVER", True, (255, 0, 0))
	text_rect = text.get_rect()
	print text_rect
	screen.blit(text, [width/2-((text_rect.right - text_rect.left)/2),height/2])
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
	for i in range(len(snake)):
		pygame.draw.rect(screen, black, snake[i], 0)
	
	for part in range(len(snake)-1):
		idx = snake[len(snake)-1].colliderect(snake[part])
		if idx != 0:
			gameOver("self")
			gameExit = True;

	for i in range(num_apples):
		screen.blit(appleimage, num_pos[i])
		 
	# idx = head.collidelist(snake)
	# if(idx < 0):
	# 	print idx

	pygame.display.update()
