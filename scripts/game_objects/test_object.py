import pygame

from scripts.graphics import SpriteSheet


class TestObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image_name):
        super(TestObject, self).__init__()
        sheet = SpriteSheet()
        self.image = sheet.get_image(image_name, scale=(32, 31))
        self.rect = self.image.get_rect(topleft=(x, y))
