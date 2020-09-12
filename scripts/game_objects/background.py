import pygame


class BackGround(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super(BackGround, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
