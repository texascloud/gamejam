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
snake = [(x_pos, y_pos)]
for x in range(50):
	snake.append((x_pos-snakeSize, y_pos))

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

	
	snake[len(snake)-1] = (x_pos, y_pos)

	if x_pos < 0 or x_pos > width:
		gameExit = True
	if y_pos < 0 or y_pos > height:
		gameExit = True

	screen.fill(white)
	for i in range(len(snake)):
		pygame.draw.rect(screen, black, [snake[i][0], snake[i][1], snakeSize, snakeSize], 0)
	
	pygame.display.flip()

