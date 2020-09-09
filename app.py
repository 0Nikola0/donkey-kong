import pygame


screenWidth, screenHeight = 800, 600
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((50, 50, 50))
    pygame.display.flip()
