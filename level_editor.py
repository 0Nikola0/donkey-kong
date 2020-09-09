import pygame


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
        pygame.draw.rect(screen, Green if self.type == 1 else Blue if self.type == 2 else Red if self.type == 3
                        else White , self.rect, 1 if self.available else 0)
        # For when I add texture to the tiles
        """
        if not self.available:
            screen.blit(tiles_img, self.pos)
        else:
            pygame.draw.rect(screen, Green, self.rect, 1)
        """


def save_tiles(s_tiles: list, tiles_type: str, lvl: str):
    # Level folder must exist before saving the tiles in selected folder
    """
    s_tiles ex: tiles1[]
    tiles_type ex: ladders
    lvl ex: 01
    """
    # Saves the pos of the occupied type X tiles
    with open(f"level{lvl}/{tiles_type}.tiles", "w") as file:
        for s_tile in s_tiles:
            file.write(str(s_tile) + ", ")


White = (255, 255, 255)
Gray = (50, 50, 50)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
screenWidth, screenHeight = 800, 600
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Creating grid of xTiles
tiles = []
tile_posx, tile_posy, tile_size = 0, 0, 50
for ver in range(12):
    for hor in range(16):
        tiles.append(Tiles((tile_posx, tile_posy), (tile_size, tile_size)))
        tile_posx += tile_size
    tile_posy += tile_size   # Changing the y pos to the next line
    tile_posx = 0     # Resetting the x pos so it is from the starting position again

tiles1 = []
tiles2 = []
tiles3 = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for tile in tiles:
                tile.clicked(event)
         # If "S" pressed on keyboard it will save all selected tiles in .lvl file
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                print("Clicked S(ave)")
                for tile in tiles:
                    # Append tiles pos to correct list if tile is occupied
                    if not tile.available:
                        if tile.type == 1:
                            tiles1.append(tile.pos)
                        elif tile.type == 2:
                            tiles2.append(tile.pos)
                        else:
                            tiles3.append(tile.pos)
                save_tiles(tiles1, tiles_type="dirt", lvl="01")
                save_tiles(tiles2, tiles_type="ladders", lvl="01")
                save_tiles(tiles3, tiles_type="lava", lvl="01")
                # Flash white screen when level is saved
                screen.fill(White)
                pygame.display.flip()
                print("Saved")

    
    screen.fill(Gray)
    for tile in tiles:
        tile.draw()
    pygame.display.flip()
