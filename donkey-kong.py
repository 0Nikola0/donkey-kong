import pygame

from scripts.game_objects.platform import Platform
from scripts.game_objects.player import Player
from scripts.game_objects.tiles import Tiles
from scripts.graphics import SpriteSheet
import settings as s

# __init__
screenWidth, screenHeight = s.SCREEN_WIDTH, s.SCREEN_HEIGHT
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

loaded_tiles = s.level_loader(s.LEVEL01)
tiles = []
for tile in loaded_tiles:
    tiles.append(Tiles(tile["type"], tile["pos"]))

platform = Platform()
player = Player(400, 300)

# ROCK DEMO
sheet = SpriteSheet()
rock = sheet.get_image('rock', scale=(32, 31))
# ROCK DEMO

running = True
while running:
    clock.tick(s.FPS)
    # If no delay the game moves too fast
    pygame.time.delay(30)
    screen.fill(s.GRAY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    player.move(keys)
    player.gravity(platform)

    # ROCK DEMO
    for x in range(0, 640, 32):
        screen.blit(rock, (x, 350))
    # ROCK DEMO

    # The player doesnt interact with the tiles yet, it does with the platform
    for tile in tiles:
        tile.display(screen)
    # platform.display()
    player.display(screen)
    pygame.display.flip()

pygame.quit()
