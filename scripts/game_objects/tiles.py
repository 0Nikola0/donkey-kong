import pygame
import settings as s


class Tiles:
    def __init__(self, tile_type, pos):
        self.sizex, self.sizey = s.TILE_SIZE, s.TILE_SIZE
        self.posx, self.posy = pos
        self.type = tile_type
        self.rect = pygame.Rect(self.posx, self.posy, self.sizex, self.sizey)

    def display(self, screen):
        # Draws empty green rect if available and blue filled if not
        pygame.draw.rect(screen, s.GREEN if self.type == 1 else s.BLUE if
                         self.type == 2 else s.RED if self.type == 3 else s.WHITE, self.rect)
        # For when we add texture to the tiles
        """
        if not self.available:
            screen.blit(tiles_img, self.pos)
        else:
            pygame.draw.rect(screen, Green, self.rect, 1)
        """
