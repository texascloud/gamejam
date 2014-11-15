import sys, pygame
pygame.init()

pygame.display.set_caption('Snake Solver')
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

speed = [1, 0]
black = 0, 0, 0
white = 255, 255, 255

gameExit = False
snake = [0, 0, 50, 50]

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		#elif event.type == KEYDOWN:
	screen.fill(white)
	pygame.draw.rect(screen, black, snake, 0)
	pygame.display.flip()

