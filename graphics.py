"""
usage:
    sheet = spritesheet.SpriteSheet()
    image = sheet.get_image('player_idle', scale=(x,y))
"""

import pygame

file_name = "resources/images/monkeylad_further.png"

NAME = {
    'player_idle':  (448, 208, 16, 24),
    'player_right':  (448 + 16, 208, 16, 24),
    'rock': (880, 16, 16, 16),
}


class SpriteSheet:
    def __init__(self):
        self.source_image = pygame.image.load(file_name).convert_alpha()

    def get_image(self, name, scale=False):
        image = self.get_image_by_coordinates(*NAME[name])
        if scale:
            image = pygame.transform.scale(image, scale)

        return image

    def get_image_by_coordinates(self, x, y, width, height):
        image = pygame.Surface([width, height], pygame.SRCALPHA)
        image.blit(self.source_image, (0, 0), (x, y, width, height))

        return image
