import pygame
import json
import settings as s
from scripts.game_objects.background import BackGround
from scripts.main_loop import MainLoop
from scripts.level_editor_objects.tiles import Tiles
import os


def save_tiles(s_tiles: list, lvl: str):
    """Saves the pos of the occupied type X tiles

    Level folder must exist before saving the tiles in selected folder
    """
    dir_path = f"../level{lvl}"
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    json_file = open(f"{dir_path}/tiles.json", "w")
    json.dump(s_tiles, json_file)


class LevelEditor(MainLoop):
    def __init__(self):
        super(LevelEditor, self).__init__('Lever Editor', s.SCREEN_SIZE, s.FRAME_RATE)
        self.background = pygame.sprite.Group()
        self.create_background()
        self.tiles = pygame.sprite.Group()
        self.create_grip()

        self.k_save = s.K_SAVE
        self.keyup_handlers[s.K_SAVE].append(self.handle_keyup)

    def create_background(self):
        self.background.add(BackGround(
            s.SCREEN_WIDTH,
            s.SCREEN_HEIGHT,
            s.GRAY,
        ))
        self.all_objects_groups.append(self.background)

    def create_grip(self):
        for ver in range(s.NUM_TILES_IN_COLUMN):
            for hor in range(s.NUM_TILES_IN_ROW):
                t = Tiles((hor * s.TILE_SIZE, ver * s.TILE_SIZE))
                self.tiles.add(t)
                self.mouse_handlers.append(t.handle_mouse_event)
        self.all_objects_groups.append(self.tiles)

    def handle_keyup(self, key):
        if key == self.k_save:
            self.save()

    def save(self):
        """If "S" pressed on keyboard it will save all selected tiles in .json file"""
        print("Clicked S(ave)")
        saved_tiles = []
        for tile in self.tiles.sprites():
            # Append tiles pos to correct list if tile is occupied
            if not tile.is_available:
                tiles_attr = {"type": tile.tile_type, "pos": tile.rect.topleft}
                saved_tiles.append(tiles_attr)
        save_tiles(saved_tiles, lvl="02")
        print(saved_tiles)
        # Flash white screen when level is saved
        self.surface.fill(s.WHITE)
        pygame.display.flip()
        pygame.time.wait(100)
        print("Saved")


def main():
    LevelEditor().run()


if __name__ == '__main__':
    main()
