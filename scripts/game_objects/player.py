import pygame
import settings as s
from scripts.graphics import SpriteSheet


class Player:
    def __init__(self, x, y):
        self.posx, self.posy = x, y
        self.sizex, self.sizey = s.PLAYER_SIZE
        self.rect = pygame.Rect(self.posx, self.posy, self.sizex, self.sizey)
        self.vel = 10
        # The jumping code is from a tutorial i watched a while ago, idk if there's a better way to do it -Nikola
        self.isJump = False
        self.jumpHeight = 10
        self.jumpCount = self.jumpHeight

        # Load the sprites and set self to idle
        sheet = SpriteSheet()
        self.image_idle = sheet.get_image('player_idle', scale=(self.sizex, self.sizey))
        self.image_right = sheet.get_image('player_right', scale=(self.sizex, self.sizey))
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_idle

    def move(self, pkeys):
        # Updating the player position based on which button is pressed
        if pkeys[pygame.K_a] and self.posx - 5 > 0:
            self.posx -= self.vel
            self.rect.topleft = (round(self.posx), round(self.posy))
            self.image = self.image_left
        if pkeys[pygame.K_d] and self.posx + self.sizex + 5 < s.SCREEN_WIDTH:
            self.posx += self.vel
            self.rect.topleft = (round(self.posx), round(self.posy))
            self.image = self.image_right
        # Space is only registered if you're not already in jump
        if not self.isJump:
            if pkeys[pygame.K_SPACE]:
                self.isJump = True
        if self.isJump:
            if self.jumpCount >= -self.jumpHeight:
                self.posy -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                # This is jump speed, i think (for some reason it breaks on 3 and you can double jump)
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = self.jumpHeight
            self.rect.topleft = (round(self.posx), round(self.posy))

    def gravity(self, platform):
        # Jumping feature already pulls the player down if in jump so this runs only if player is not in jump
        if not self.isJump:
            if self.posy + self.sizey < platform.posy:
                self.posy += s.GRAVITY
            # If the player glitches and his position is below the platform this puts him on top of it
            if self.posy + self.sizey > platform.posy:
                self.posy = platform.posy - self.sizey
            self.rect.topleft = (round(self.posx), round(self.posy))

    def display(self, screen):
        # pygame.draw.rect(screen, Blue, self.rect)
        screen.blit(self.image, self.rect)