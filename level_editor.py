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


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for tile in tiles:
                tile.clicked(event)
    
    screen.fill(Gray)
    for tile in tiles:
        tile.draw()
    pygame.display.flip()
