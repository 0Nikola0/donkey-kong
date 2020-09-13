import pygame
from pygame.math import Vector2

import settings as s
from scripts.graphics import SpriteSheet


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, keys):
        super(Player, self).__init__()
        self.posx, self.posy = x, y
        self.sizex, self.sizey = s.PLAYER_SIZE

        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        # The jumping code is from a tutorial i watched a while ago, idk if there's a better way to do it -Nikola
        self.isJump = False
        self.jumpHeight = 10
        self.jumpCount = self.jumpHeight

        self.is_stand_on_tile = False

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
        self.is_stand_on_tile = not state

    def physics(self):
        self.acc = Vector2(0, 0)

        if self.is_stand_on_tile is False:
            self.acc.y = s.PLAYER_GRAVITY
        else:
            self.vel.y = 1  # It will entail collision and remain is_stand_on_tile in True state.

        if self.is_move_left is True:
            self.acc.x = -s.PLAYER_ACCELERATION
            self.change_image("image_left")
        if self.is_move_right is True:
            self.acc.x = s.PLAYER_ACCELERATION
            self.change_image("image_right")

        if self.is_jump and self.is_stand_on_tile:
            self.jump()
        else:
            self.is_jump = False

        self.acc.x += self.vel.x * s.PLAYER_FRICTION
        self.vel += self.acc

    def jump(self):
        self.vel.y = -s.PLAYER_JUMP_HEIGHT

    def update(self, *args):
        """Move player if he jumped or have velocity"""
        self.physics()

        self.rect.move_ip((self.vel.x + (0.5 * self.acc.x), self.vel.y))  # in x - kinematics formula

    def change_image(self, image_name):
        if image_name == "image_right":
            self.image = self.image_right
        elif image_name == "image_left":
            self.image = self.image_left
        elif image_name == "image_idle":
            self.image = self.image_idle
