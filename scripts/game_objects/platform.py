import pygame
import settings as s


# Need to replace platform with tiles, but i dont know if i can do the collisions correct -Nikola
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super(Platform, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
