import json
import pygame

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Screen size
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = 800, 600

# FPS
FRAME_RATE = 30

# Sprites and tiles
TILE_SIZE = 50

NUM_TILES_IN_ROW = SCREEN_WIDTH // TILE_SIZE
NUM_TILES_IN_COLUMN = SCREEN_HEIGHT // TILE_SIZE

# Global physics
GRAVITY = 0, -1000
BASIC_FRICTION = .5
BASIC_ELASTICITY = 1

# Player properties
PLAYER_SIZE = (PLAYER_SIZE_X, PLAYER_SIZE_Y) = 40, 60
PLAYER_SHAPE_RADIUS = 5

PLAYER_MOVE_FORCE = 250
PLAYER_JUMP_IMPULSE = 600

PLAYER_FRICTION = .05
PLAYER_ELASTICITY = BASIC_ELASTICITY

# Tiles properties
TILE_FRICTION = BASIC_FRICTION
TILE_ELASTICITY = .3

# levels
LEVEL01 = "level01"


def level_loader(lvl):
    file = open(f"levels/{lvl}/tiles.json")
    l_tiles = json.load(file)
    return l_tiles


def flip_y(pos):
    """Convert pymunk physics to pygame coordinates

    In pymunk positive y is up
    """
    # if type(pos) is tuple or type(pos) is list:
    try:
        return pos[0], SCREEN_HEIGHT - pos[1]
    except TypeError:
        # else:
        y = pos
        return SCREEN_HEIGHT - y


# # Controllers # #
# Player
K_PLAYER_MOVE_LEFT = pygame.K_a
K_PLAYER_MOVE_RIGHT = pygame.K_d
K_PLAYER_JUMP = pygame.K_SPACE

# Lever editor
K_SAVE = pygame.K_s
