import pygame
from scripts import settings as s


class Tiles(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos):
        super(Tiles, self).__init__()
        self.image = self.get_test_image(tile_type)
        self.rect = self.image.get_rect(topleft=pos)

    @staticmethod
    def get_test_image(type):
        if type == 1:
            color = s.GREEN
        elif type == 2:
            color = s.BLUE
        elif type == 3:
            color = s.RED
        else:
            color = s.WHITE
        image = pygame.Surface((s.TILE_SIZE, s.TILE_SIZE))
        image.fill(color)

        if color == s.WHITE:
            inner_color = pygame.Surface((s.TILE_SIZE, s.TILE_SIZE))
            inner_color.fill(s.GRAY)
            image.blit(inner_color, (1, 1))

        return image
