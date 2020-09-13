import pygame

from scripts.game_objects.background import BackGround
from scripts.game_objects.player import Player
from scripts.game_objects.test_object import TestObject
from scripts.game_objects.tiles import Tiles
from scripts.graphics import SpriteSheet
from scripts.main_loop import MainLoop
import settings as s


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

        self.create_objects()

    def create_objects(self):
        self.create_background()
        self.create_map()
        self.create_player()

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

        hits = pygame.sprite.groupcollide(self.tiles, self.player, False, False)
        if hits:
            player = self.player.sprite
            for tile in hits:
                if tile.rect.top < player.rect.bottom:  # if tile behind the player / 1-side collision
                    self.player.sprite.rect.bottom = tile.rect.top
                    self.player.sprite.activate_gravity(False)
        else:
            self.player.sprite.activate_gravity(True)

        if self.player.sprite.rect.bottom > s.SCREEN_HEIGHT:  # debug if player falls outer screen
            self.player.sprite.rect.topleft = self.player_spawn
            self.player.sprite.activate_gravity(True)


def main():
    DonkeyKong().run()


if __name__ == '__main__':
    main()
