import pygame

from scripts.game_objects.background import BackGround
from scripts.game_objects.enemy import TestEnemy
from scripts.game_objects.player import Player
from scripts.game_objects.test_object import TestObject
from scripts.game_objects.tiles import Tiles
from scripts.main_loop import MainLoop
from scripts import settings as s


class DonkeyKong(MainLoop):
    def __init__(self):
        super(DonkeyKong, self).__init__("Donkey Kong", s.SCREEN_SIZE, s.FRAME_RATE)

        # self.sheet = SpriteSheet()
        self.player_spawn = (400, 300)

        # Groups
        self.background = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.platform = pygame.sprite.GroupSingle()
        self.tiles = pygame.sprite.Group()
        self.__test_tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.create_objects()

    def create_objects(self):
        self.create_background()
        self.create_map()
        self.create_player()
        self.create_enemies()

    def create_background(self):
        self.background.add(BackGround(
            s.SCREEN_WIDTH,
            s.SCREEN_HEIGHT,
            s.GRAY,
        ))
        self.all_objects_groups.append(self.background)

    def create_map(self):
        self.create_tiles()
        self.create_test_tiles()

    def create_tiles(self):
        loaded_tiles = s.level_loader(s.LEVEL01)
        for tile in loaded_tiles:
            self.tiles.add(Tiles(tile["type"], tile["pos"]))
        self.all_objects_groups.append(self.tiles)

    def create_test_tiles(self):
        for x in range(0, 640, 32):
            self.__test_tiles.add(TestObject(
                x,
                350,
                'rock'
            ))
        self.all_objects_groups.append(self.__test_tiles)

    def create_enemies(self):
        self.enemies.add(TestEnemy(100, 50))
        self.all_objects_groups.append(self.enemies)

    def create_player(self):
        player_controllers = {
            'move_left': s.K_PLAYER_MOVE_LEFT,
            'move_right': s.K_PLAYER_MOVE_RIGHT,
            'jump': s.K_PLAYER_JUMP,
        }

        player = Player(
            self.player_spawn[0],
            self.player_spawn[1],
            keys=player_controllers,
            is_stand_on_tile=False,
        )
        for key in player_controllers.values():
            self.add_up_down_key_handlers(player, key)

        self.player.add(player)
        self.all_objects_groups.append(self.player)

    def update(self):
        super().update()

        self.player_tile_collisions()

    def player_tile_collisions(self):
        """Change player physics if he collides with a tile

        Because of multiple collisions, we need to find the lowest
        tile (for top-collision), highest tile (for bot-collision)

        Top and bottom collisions cannot occur at the same time
        and
        Left and right collisions cannot occur at the same time
        but
        Top or bottom collision can occur simultaneously with the left or right
        """
        hits = pygame.sprite.groupcollide(self.tiles, self.player, False, False)
        if hits:
            player = self.player.sprite
            lowest_tile = highest_tile = left_tile = right_tile = list(hits)[0]
            for tile in hits:
                if lowest_tile.rect.y < tile.rect.y:
                    lowest_tile = tile
                if highest_tile.rect.y > tile.rect.y:
                    highest_tile = tile
            for tile in hits:
                if left_tile.rect.x >= tile.rect.x and tile.rect.y not in (lowest_tile.rect.y, highest_tile.rect.y):
                    left_tile = tile
                if right_tile.rect.x <= tile.rect.x and tile.rect.y not in (lowest_tile.rect.y, highest_tile.rect.y):
                    right_tile = tile

            # Affect player physics if collision
            if player.is_move_right() and right_tile.rect.y not in (lowest_tile.rect.y, highest_tile.rect.y):
                if right_tile.rect.left < player.rect.right:
                    player.rect.right = right_tile.rect.left
                    player.stop_right_moving()
            elif player.is_move_left() and left_tile.rect.y not in (lowest_tile.rect.y, highest_tile.rect.y):
                if left_tile.rect.left < player.rect.right:
                    player.rect.left = left_tile.rect.right
                    player.stop_left_moving()

            if player.is_falling():  # if player is falling
                if lowest_tile.rect.top < player.rect.bottom:
                    player.rect.bottom = lowest_tile.rect.top
                    player.activate_gravity(False)
            elif player.is_jumping():  # player is jumping (going upwards to the screen)
                if highest_tile.rect.bottom < player.rect.bottom:
                    player.rect.top = highest_tile.rect.bottom
                    player.stop_jumping()

        else:  # if the player doesn't hit a tile, then he is falling
            self.player.sprite.activate_gravity(True)

        if self.player.sprite.rect.bottom > s.SCREEN_HEIGHT:  # debug if player falls outer screen
            self.player.sprite.rect.topleft = self.player_spawn
            self.player.sprite.activate_gravity(True)


def main():
    DonkeyKong().run()


if __name__ == '__main__':
    main()
