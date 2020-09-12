import pygame
from scripts.game_objects.tiles import Tiles


class Tiles(Tiles):
    PRESSED = "pressed"
    NORMAL = "normal"

    def __init__(self, pos):
        self.state = self.NORMAL
        self.tile_type = 0
        self.available = True
        super().__init__(self.tile_type, pos)

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

    def update(self):
        self.image = self.get_test_image(self.tile_type)
