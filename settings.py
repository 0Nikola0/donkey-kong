import json
import pygame


# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen size
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = 800, 600

# FPS
FRAME_RATE = 30

# Sprites and tiles
TILE_SIZE = 50

NUM_TILES_IN_ROW = SCREEN_WIDTH // TILE_SIZE
NUM_TILES_IN_COLUMN = SCREEN_HEIGHT // TILE_SIZE

# Physics
GLOBAL_GRAVITY = 15

# Player properties
PLAYER_SIZE = (PLAYER_SIZE_X, PLAYER_SIZE_Y) = 40, 60
PLAYER_ACCELERATION = 0.8
PLAYER_FRICTION = -0.07
# player max velocity.x ~=~ 11
PLAYER_GRAVITY = GLOBAL_GRAVITY  # How fast the player falls (how fast is the player pulled to the ground)

# levels
LEVEL01 = "level01"


def level_loader(lvl):
    file = open(f"{lvl}/tiles.json")
    l_tiles = json.load(file)
    return l_tiles


# # Controllers # #
# Player
K_PLAYER_MOVE_LEFT = pygame.K_a
K_PLAYER_MOVE_RIGHT = pygame.K_d
K_PLAYER_JUMP = pygame.K_SPACE

# Lever editor
K_SAVE = pygame.K_s
