import pygame
from scripts import settings as s


class TestEnemy(pygame.sprite.Sprite):
    """Very evil and scary"""
    def __init__(self, x, y):
        super(TestEnemy, self).__init__()
        self.image = pygame.Surface((s.TILE_SIZE, s.TILE_SIZE))
        self.image.fill(s.YELLOW)
        self.rect = self.image.get_rect(topleft=(x, y))
