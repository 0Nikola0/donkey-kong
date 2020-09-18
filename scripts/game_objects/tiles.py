import pygame
import pymunk

from scripts import settings as s


class Tiles(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos, space):
        # physics stuff
        self.body = space.static_body
        pos_x, pos_y = s.flip_y(pos)
        self.body.position = pos_x + s.TILE_SIZE // 2, pos_y - s.TILE_SIZE // 2  # body.position == rect.center
        self.shape = pymunk.Poly.create_box(self.body, (s.TILE_SIZE, s.TILE_SIZE))
        self.shape.friction = s.TILE_FRICTION
        self.shape.elasticity = s.TILE_ELASTICITY
        space.add(self.shape)

        # pygame stuff
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
