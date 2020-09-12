import pygame
import settings as s
from scripts.graphics import SpriteSheet


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, keys, platform):
        super(Player, self).__init__()
        self.posx, self.posy = x, y
        self.sizex, self.sizey = s.PLAYER_SIZE

        self.platform = platform

        self.vel = 10
        self.current_vel = 0

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

    def handle_key_down(self, key):
        if key == self.k_move_left:
            self.current_vel = -self.vel
            self.image = self.image_left
        elif key == self.k_move_right:
            self.current_vel = self.vel
            self.image = self.image_right
        elif key == self.k_jump and not self.isJump:
            self.isJump = True

    def handle_key_up(self, key):
        if key == self.k_move_left:
            self.current_vel = 0
        elif key == self.k_move_right:
            self.current_vel = 0

    def update(self, *args):
        """Move player if he jumped or have velocity"""
        # TODO: Fix key_up, key_down functions. If player press both keys and then up one of them
        #  self.current_vel will be == 0 (even player still hold the opposing move_key)
        if self.current_vel > 0:  # move right case
            if self.rect.right + 5 < s.SCREEN_WIDTH:
                self.rect.move_ip((self.current_vel, 0))
        elif self.current_vel < 0:  # move left case
            if self.rect.left - 5 > 0:
                self.rect.move_ip((self.current_vel, 0))

        if self.isJump:  # jump case or jump + move case
            if self.jumpCount >= -self.jumpHeight:
                jump_speed = (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.rect.move_ip((0, -jump_speed))
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = self.jumpHeight

        elif not self.isJump:  # gravity case
            if self.current_vel == 0:
                self.image = self.image_idle
            if self.rect.bottom < self.platform.rect.top:
                self.rect.move_ip((0, s.GRAVITY))
            # If the player glitches and his position is below the platform this puts him on top of it
            if self.rect.bottom > self.platform.rect.top:
                self.rect.bottom = self.platform.rect.top
