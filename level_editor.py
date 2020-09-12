import pygame
import json
import settings as s

class Tiles:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.available = True
        self.type = 0

    def clicked(self, ev):
        if self.rect.collidepoint(ev.pos[0], ev.pos[1]):
            # Changing the availability on click (if available and clicked it changes to not available and vice versa)
            self.type = (self.type + 1) if self.type < 3 else 0
            self.available = True if self.type == 0 else False

    def draw(self):
        # Draws empty green rect if available and blue filled if not
        pygame.draw.rect(screen, s.GREEN if self.type == 1 else s.BLUE if self.type == 2 else s.RED if self.type == 3
                         else s.WHITE, self.rect, 1 if self.available else 0)
        # For when I add texture to the tiles
        """
        if not self.available:
            screen.blit(tiles_img, self.pos)
        else:
            pygame.draw.rect(screen, Green, self.rect, 1)
        """


def save_tiles(s_tiles: list, lvl: str):
    # Level folder must exist before saving the tiles in selected folder
    # Saves the pos of the occupied type X tiles
    json_file = open(f"level{lvl}/tiles.json", "w")
    json.dump(s_tiles, json_file)


screen_size = s.SCREEN_SIZE
pygame.init()
pygame.display.set_caption("Level Editor")
screen = pygame.display.set_mode(screen_size)

# Creating grid of xTiles
tiles = []
tile_posx, tile_posy = 0, 0
tile_size = s.TILE_SIZE
for ver in range(12):
    for hor in range(16):
        tiles.append(Tiles((tile_posx, tile_posy), (tile_size, tile_size)))
        tile_posx += tile_size
    tile_posy += tile_size  # Changing the y pos to the next line
    tile_posx = 0  # Resetting the x pos so it is from the starting position again


saved_tiles = []

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(s.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for tile in tiles:
                tile.clicked(event)
        # If "S" pressed on keyboard it will save all selected tiles in .json file
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                print("Clicked S(ave)")
                for tile in tiles:
                    # Append tiles pos to correct list if tile is occupied
                    if not tile.available:
                        tiles_attr = {"type": tile.type, "pos": tile.pos}
                        saved_tiles.append(tiles_attr)
                save_tiles(saved_tiles, lvl="01")
                print(saved_tiles)
                # Flash white screen when level is saved
                screen.fill(s.WHITE)
                pygame.display.flip()
                print("Saved")

    screen.fill(s.GRAY)
    for tile in tiles:
        tile.draw()
    pygame.display.flip()
