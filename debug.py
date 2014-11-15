import sys, pygame, random
pygame.init()
class NumberGrid(object):
	def __init__(self, amount):
		self.length = amount
		self.numList = []
	def populate(self):
		return 0

def position_generator(amount):
	numList = []
	for i in range(amount):
		applepos = (random.randint(0, 590), random.randint(0, 590))
		numList.append(applepos)
	return numList
def make_tuples(amount):
	dict = {}
	for i in range(amount):
		applepos = (random.randint(0, 590), random.randint(0, 590))
		dict[applepos] = i

	for key in dict.keys():
		print key


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
applepos = (random.randint(0, 590), random.randint(0, 590))
num_apples = 9
num_pos = position_generator(num_apples)
#make_tuples(num_apples)
appleimage = pygame.Surface((10, 10))
appleimage.fill((0, 255, 0))

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
	for i in range(num_apples):
		screen.blit(appleimage, num_pos[i])
	pygame.display.flip()

