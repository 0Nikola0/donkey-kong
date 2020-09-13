import pygame
from pygame.math import Vector2

import settings as s
from scripts.graphics import SpriteSheet


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, keys, platform):
        super(Player, self).__init__()
        self.posx, self.posy = x, y
        self.sizex, self.sizey = s.PLAYER_SIZE

        self.platform = platform

        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        # The jumping code is from a tutorial i watched a while ago, idk if there's a better way to do it -Nikola
        self.isJump = False
        self.jumpHeight = 10
        self.jumpCount = self.jumpHeight

        # Load the sprites and set self to idle
        sheet = SpriteSheet()
        self.image_idle = sheet.get_image('player_idle', scale=s.PLAYER_SIZE)
        self.image_right = sheet.get_image('player_right', scale=s.PLAYER_SIZE)
        self.image_left = pygame.transform.flip(self.image_right, True, False)

        self.image = self.image_idle
        self.rect = self.image.get_rect(topleft=(self.posx, self.posy))

        # Assign keys
        self.k_move_left = keys['move_left']
        self.k_move_right = keys['move_right']
        self.k_jump = keys['jump']

        self.acc_down = False
        self.move_left = False
        self.move_right = False

    def handle_key_down(self, key):
        if key == self.k_move_left:
            self.move_left = True
            self.image = self.image_left
        if key == self.k_move_right:
            self.move_right = True
            self.image = self.image_right
        elif key == self.k_jump and not self.isJump:
            self.isJump = True

    def handle_key_up(self, key):
        if key == self.k_move_left:
            self.move_left = False

        if key == self.k_move_right:
            self.move_right = False

    def movement_physics(self):
        self.acc = Vector2(0, 0)
        if self.move_left is True:
            self.acc.x = -s.PLAYER_ACCELERATION
            self.change_image("image_left")
        if self.move_right is True:
            self.acc.x = s.PLAYER_ACCELERATION
            self.change_image("image_right")

        self.acc += self.vel * s.PLAYER_FRICTION
        self.vel += self.acc

    def update(self, *args):
        """Move player if he jumped or have velocity"""
        self.movement_physics()
        if self.vel.x > 0:
            if self.rect.right + 5 < s.SCREEN_WIDTH:  # move right case
                self.rect.move_ip((self.vel.x + (0.5 * self.acc.x), 0))
        elif self.vel.x < 0:
            if self.rect.left - 5 > 0:  # move left case
                self.rect.move_ip((self.vel.x + (0.5 * self.acc.x), 0))

        if self.isJump:  # jump case or jump + move case
            if self.jumpCount >= -self.jumpHeight:
                jump_speed = (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.rect.move_ip((0, -jump_speed))
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = self.jumpHeight

        elif not self.isJump:  # gravity case
            if self.rect.bottom < self.platform.rect.top:
                self.rect.move_ip((0, s.GLOBAL_GRAVITY))
            # If the player glitches and his position is below the platform this puts him on top of it
            if self.rect.bottom > self.platform.rect.top:
                self.rect.bottom = self.platform.rect.top

        # self.physics()

    def change_image(self, image_name):
        if image_name == "image_right":
            self.image = self.image_right
        elif image_name == "image_left":
            self.image = self.image_left
        elif image_name == "image_idle":
            self.image = self.image_idle
