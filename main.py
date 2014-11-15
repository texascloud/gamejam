import sys, pygame
from pygame.locals import *
pygame.init()

pygame.display.set_caption('Snake Solver')
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
speed = 2
snakeSize = 10
x_speed = speed
y_speed = 0


black = 0, 0, 0
white = 255, 255, 255

gameExit = False
x_pos = 300
y_pos = 300
head = pygame.Rect(x_pos, y_pos, snakeSize, snakeSize)
snake = [head]
for x in range(10):
	body = pygame.Rect(x_pos-(snakeSize*x), y_pos, snakeSize, snakeSize)
	snake.append(body)

fps = 120


while not gameExit:
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT and x_speed == 0:
				x_speed = -speed
				y_speed = 0
			if event.key == pygame.K_RIGHT and x_speed == 0:
				x_speed = speed
				y_speed = 0
			if event.key == pygame.K_UP and y_speed == 0:
				x_speed = 0
				y_speed = -speed
			if event.key == pygame.K_DOWN and y_speed == 0:
				x_speed = 0
				y_speed = speed

	x_pos += x_speed
	y_pos += y_speed

	for i in range(len(snake)-1):
		snake[i] = snake[i+1]

	
	snake[len(snake)-1] = pygame.Rect(x_pos, y_pos, snakeSize, snakeSize)

	if x_pos < 0 or x_pos > width:
		gameExit = True
	if y_pos < 0 or y_pos > height:
		gameExit = True

	screen.fill(white)
	for i in range(len(snake)):
		print snake[i]
		pygame.draw.rect(screen, black, snake[i], 0)
	
	if(pygame.Rect.collidelist(snake) < 0):
		gameExit = True
	pygame.display.flip()

