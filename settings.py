import json
# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen size
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = 800, 600

# FPS
FPS = 30

# Sprites
TILE_SIZE = 50
PLAYER_SIZE = (PLAYER_SIZE_X, PLAYER_SIZE_Y) = 40, 60

# Physics
GRAVITY = 15  # How fast the player falls (how fast is the player pulled to the ground)

# levels
LEVEL01 = "level01"


def level_loader(lvl):
    file = open(f"{lvl}/tiles.json")
    l_tiles = json.load(file)
    return l_tiles
