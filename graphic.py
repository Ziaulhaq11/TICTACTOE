import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

running = True

while running:
	screen.fill((55,21,32))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()