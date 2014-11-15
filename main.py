import sys, pygame
from pygame.locals import *
pygame.init()

pygame.display.set_caption('Snake Solver')
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
speed = 2
x_speed = speed
y_speed = 0

black = 0, 0, 0
white = 255, 255, 255

gameExit = False
x_pos = 300
y_pos = 300
snake = [0, 0, 50, 50]
fps = 120

while not gameExit:
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_speed = -speed
				y_speed = 0
			if event.key == pygame.K_RIGHT:
				x_speed = speed
				y_speed = 0
			if event.key == pygame.K_UP:
				x_speed = 0
				y_speed = -speed
			if event.key == pygame.K_DOWN:
				x_speed = 0
				y_speed = speed

	x_pos += x_speed
	y_pos += y_speed

	if x_pos < 0 or x_pos > width:
		x_speed = -x_speed
	if y_pos < 0 or y_pos > height:
		y_speed = -y_speed

	screen.fill(white)
	pygame.draw.rect(screen, black, [x_pos, y_pos, 5, 5], 0)
	pygame.display.flip()

