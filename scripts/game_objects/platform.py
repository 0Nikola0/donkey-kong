import pygame
import settings as s


# Need to replace platform with tiles, but i dont know if i can do the collisions correct -Nikola
class Platform:
    def __init__(self):
        self.posx, self.posy = 0, s.SCREEN_HEIGHT - 20  # 20 pixels above the bottom border
        self.sizex, self.sizey = s.SCREEN_WIDTH, 20
        self.rect = pygame.Rect(self.posx, self.posy, self.sizex, self.sizey)

    def display(self, screen):
        pygame.draw.rect(screen, s.GREEN, self.rect)
