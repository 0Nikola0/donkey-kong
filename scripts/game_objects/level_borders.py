import pygame
import pymunk
from scripts.settings import flip_y


class LevelBorders:
    def __init__(self, space, level_width, level_height, d=5):
        """"""
        x0, y0 = 0, 0
        x1, y1 = level_width, level_height
        pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        for i in range(4):
            segment = pymunk.Segment(space.static_body, pts[i], pts[(i + 1) % 4], d)
            segment.elasticity = 1
            segment.friction = 1
            space.add(segment)
