import sys, pygame
pygame.init()

pygame.display.set_caption('Snake Solver')
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

speed = [1, 0]
black = 0, 0, 0
white = 255, 255, 255

gameExit = False
start_x = 300
start_y = 300
snake = [0, 0, 50, 50]

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				start_x -= 5
			if event.key == pygame.K_RIGHT:
				start_x += 5
			if event.key == pygame.K_UP:
				start_y -= 5
			if event.key == pygame.K_DOWN:
				start_y += 5	

	screen.fill(white)
	pygame.draw.rect(screen, black, [start_x, start_y, 5, 5], 0)
	pygame.display.flip()

