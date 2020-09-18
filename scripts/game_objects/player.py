import pygame
import pymunk
from pygame.math import Vector2

from scripts import settings as s
from scripts.graphics import SpriteSheet


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, space, /, keys):
        # physics stuff
        self.body = pymunk.Body(mass=1, moment=pymunk.inf, body_type=pymunk.Body.DYNAMIC)
        pm_x, pm_y = x, s.flip_y(y)
        self.body.position = pm_x + s.PLAYER_SIZE_X // 2, pm_y - s.PLAYER_SIZE_Y // 2  # body.position == rect.center
        self.shape = pymunk.Poly.create_box(self.body, s.PLAYER_SIZE)
        self.shape.elasticity = 1
        self.friction = s.PLAYER_FRICTION
        self.shape.friction = self.friction
        space.add(self.body, self.shape)

        # pygame stuff
        super(Player, self).__init__()
        self.posx, self.posy = x, y
        self.sizex, self.sizey = s.PLAYER_SIZE

        self.force = (0, 0)  # Current force applied to the player for movement by keyboard

        self.is_stand = False

        # self.direction = 0  # 0 = idle; -1 = moving left: 1 = moving right
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

    def check_grounding(self):
        """ See if the player is on the ground. Used to see if we can jump.

        From pymunk platformer example
        """
        grounding = {
            'normal': pymunk.Vec2d.zero(),
            'penetration': pymunk.Vec2d.zero(),
            'impulse': pymunk.Vec2d.zero(),
            'position': pymunk.Vec2d.zero(),
            'body': None
        }

        def f(arbiter):
            n = -arbiter.contact_point_set.normal
            if n.y > grounding['normal'].y:
                grounding['normal'] = n
                grounding['penetration'] = -arbiter.contact_point_set.points[0].distance
                grounding['body'] = arbiter.shapes[1].body
                grounding['impulse'] = arbiter.total_impulse
                grounding['position'] = arbiter.contact_point_set.points[0].point_b

        self.body.each_arbiter(f)

        return grounding

    def handle_key_down(self, key):
        if key == self.k_move_left:
            # Add force to the player, and set the player friction to basic one
            self.force = (-s.PLAYER_MOVE_FORCE, 0)
            self.shape.friction = self.friction
            self.image = self.image_left
        if key == self.k_move_right:
            # Add force to the player, and set the player friction to basic one
            self.force = (s.PLAYER_MOVE_FORCE, 0)
            self.shape.friction = self.friction
            self.image = self.image_right
        elif key == self.k_jump:
            # find out if player is standing on ground
            grounding = self.check_grounding()
            if grounding['body'] is not None and abs(
                    grounding['normal'].x / grounding['normal'].y) < self.shape.friction:
                self.body.apply_impulse_at_local_point((0, s.PLAYER_JUMP_IMPULSE))

    def handle_key_up(self, key):
        if key == self.k_move_left:
            # Remove force from the player, and set the player friction to a high number so he stops
            self.force = (0, 0)
            self.shape.friction = 1

        if key == self.k_move_right:
            # Remove force from the player, and set the player friction to a high number so he stops
            self.force = (0, 0)
            self.shape.friction = 1

    def update(self, *args):
        self.rect.center = s.flip_y(self.body.position)  # synchronizes player rect with pymunk player shape

        # If we have force to apply to the player (from hitting the arrow keys), apply it. (left-right)
        self.body.apply_force_at_local_point(self.force, (0, 0))

    def change_image(self, image_name):
        if image_name == "image_right":
            self.image = self.image_right
        elif image_name == "image_left":
            self.image = self.image_left
        elif image_name == "image_idle":
            self.image = self.image_idle
