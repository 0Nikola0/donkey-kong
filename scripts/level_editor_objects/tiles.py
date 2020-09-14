import pygame
from scripts import settings as s


class Tiles(pygame.sprite.Sprite):
    PRESSED = "pressed"
    NORMAL = "normal"

    def __init__(self, pos):
        super(Tiles, self).__init__()
        self.state = self.NORMAL
        self.tile_type = 0
        self.available = True
        self.image = self.get_test_image(self.tile_type)
        self.rect = self.image.get_rect(topleft=pos)

    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)

    def handle_mouse_move(self, pos):
        if self.rect.collidepoint(pos):
            pass

    def handle_mouse_down(self, pos):
        if self.rect.collidepoint(pos):
            self.__change_state()

    def handle_mouse_up(self, pos):
        if self.state == self.PRESSED:
            self.on_click()
            self.__change_state()

    def __change_state(self):
        if self.state == self.PRESSED:
            self.state = self.NORMAL
        else:
            self.state = self.PRESSED

    @property
    def is_available(self):
        return self.available

    def on_click(self):
        # Changing the availability on click (if available and clicked it changes to not available and vice versa)
        self.tile_type = (self.tile_type + 1) if self.tile_type < 3 else 0
        self.available = True if self.tile_type == 0 else False

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

    def update(self):
        self.image = self.get_test_image(self.tile_type)
