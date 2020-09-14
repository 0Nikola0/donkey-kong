import pygame
from pygame.math import Vector2

import settings as s
from scripts.graphics import SpriteSheet


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, /, keys, is_stand_on_tile=False):
        super(Player, self).__init__()
        self.posx, self.posy = x, y
        self.sizex, self.sizey = s.PLAYER_SIZE

        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        self.is_stand = is_stand_on_tile

        self.is_move_left = False
        self.is_move_right = False
        self.is_jump = False

        # Assign keys
        self.k_move_left = keys['move_left']
        self.k_move_right = keys['move_right']
        self.k_jump = keys['jump']

        # Load the sprites and set self to idle
        sheet = SpriteSheet()
        self.image_idle = sheet.get_image('player_idle', scale=s.PLAYER_SIZE)
        self.image_right = sheet.get_image('player_right', scale=s.PLAYER_SIZE)
        self.image_left = pygame.transform.flip(self.image_right, True, False)

        self.image = self.image_idle
        self.rect = self.image.get_rect(topleft=(self.posx, self.posy))

    def handle_key_down(self, key):
        if key == self.k_move_left:
            self.is_move_left = True
            self.image = self.image_left
        if key == self.k_move_right:
            self.is_move_right = True
            self.image = self.image_right
        elif key == self.k_jump:
            self.is_jump = True

    def handle_key_up(self, key):
        if key == self.k_move_left:
            self.is_move_left = False

        if key == self.k_move_right:
            self.is_move_right = False

    def activate_gravity(self, state: bool):
        """On and off gravity/y-acceleration"""
        self.is_stand = not state

    def physics(self):
        """Calculates player velocity and acceleration

        If you want the Player to speed up or slow down then change these constants:
        PLAYER_ACCELERATION and PLAYER_FRICTION for player speed
        PLAYER_JUMP_HEIGHT for jump height
        """
        self.acc = Vector2(0, 0)

        if self.is_stand is False:
            self.acc.y = s.PLAYER_GRAVITY
        else:
            self.vel.y = 1  # It will entail collision and remain is_stand_on_tile in True state.

        if self.is_move_left is True:
            self.acc.x = -s.PLAYER_ACCELERATION
            self.change_image("image_left")
        if self.is_move_right is True:
            self.acc.x = s.PLAYER_ACCELERATION
            self.change_image("image_right")

        if self.is_jump and self.is_stand:
            self.jump()
        else:
            self.is_jump = False

        self.acc.x += self.vel.x * s.PLAYER_FRICTION
        self.vel += self.acc

    def jump(self):
        self.vel.y = -s.PLAYER_JUMP_HEIGHT

    def move_player(self):
        x_offset = self.vel.x + (0.5 * self.acc.x)  # kinematics formula
        y_offset = self.vel.y
        self.rect.move_ip((x_offset, y_offset))

    def update(self, *args):
        """Change player state

        This method will be called every iteration of gameloop
        """
        self.physics()
        self.move_player()

    def change_image(self, image_name):
        if image_name == "image_right":
            self.image = self.image_right
        elif image_name == "image_left":
            self.image = self.image_left
        elif image_name == "image_idle":
            self.image = self.image_idle
