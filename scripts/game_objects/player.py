import pygame
from pygame.math import Vector2

from scripts import settings as s
from scripts.graphics import SpriteSheet


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, /, keys):
        super(Player, self).__init__()
        self.posx, self.posy = x, y
        self.sizex, self.sizey = s.PLAYER_SIZE

        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        self.is_stand = False

        self.move_left_k_pressed = False
        self.move_right_k_pressed = False
        self.jumping_k_pressed = False

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
            self.move_left_k_pressed = True
            self.image = self.image_left
        if key == self.k_move_right:
            self.move_right_k_pressed = True
            self.image = self.image_right
        elif key == self.k_jump:
            self.jumping_k_pressed = True

    def handle_key_up(self, key):
        if key == self.k_move_left:
            self.move_left_k_pressed = False

        if key == self.k_move_right:
            self.move_right_k_pressed = False

    def deactivate_gravity(self):
        self.is_stand = True

    def is_falling(self):
        return self.vel.y > 0

    def is_jumping(self):
        return self.vel.y < 0

    def is_move_right(self):
        return self.vel.x > 0.5

    def is_move_left(self):
        return self.vel.x < -0.5

    def stop_jumping(self):
        self.vel.y = 0.5

    def stop_right_moving(self):
        self.vel.x = 0
        self.acc.x = 0

    def stop_left_moving(self):
        self.vel.x = 0
        self.acc.x = 0

    def jump(self):
        self.vel.y = -s.PLAYER_JUMP_HEIGHT

    def reset_collisions_variables(self):
        self.is_stand = False

    def physics(self):
        """Calculates player velocity and acceleration

        If you want the Player to speed up or slow down then change these constants:
        PLAYER_ACCELERATION and PLAYER_FRICTION for player speed
        PLAYER_JUMP_HEIGHT for jump height
        """
        self.acc = Vector2(0, 0)

        if self.is_stand is False:
            self.acc.y = s.PLAYER_GRAVITY
        elif self.is_stand is True:
            self.vel.y = 1  # It will entail collision and remain is_stand_on_tile in True state.

        if self.move_left_k_pressed is True:
            self.acc.x = -s.PLAYER_ACCELERATION
            self.change_image("image_left")
        if self.move_right_k_pressed is True:
            self.acc.x = s.PLAYER_ACCELERATION
            self.change_image("image_right")

        if self.jumping_k_pressed and self.is_stand:
            self.jump()
        else:
            self.jumping_k_pressed = False

        self.acc.x += self.vel.x * s.PLAYER_FRICTION
        self.vel += self.acc

        self.reset_collisions_variables()

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
