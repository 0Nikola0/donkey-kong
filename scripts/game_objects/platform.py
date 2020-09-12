import pygame
import settings as s


# Need to replace platform with tiles, but i dont know if i can do the collisions correct -Nikola
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
