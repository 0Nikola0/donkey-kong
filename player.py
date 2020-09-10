import pygame
from graphics import SpriteSheet


# Need to replace platform with tiles, but i dont know if i can do the collisions correct -Nikola
class Platform:
    def __init__(self):
        self.posx, self.posy = 0, screenHeight - 20     # 20 pixels above the bottom border
        self.sizex, self.sizey = screenWidth, 20         
        self.rect = pygame.Rect(self.posx, self.posy, self.sizex, self.sizey)
    
    def display(self):
        pygame.draw.rect(screen, Green, self.rect)


class Player:
    def __init__(self):
        self.posx, self.posy = 400, 300
        self.sizex, self.sizey = 40, 60
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
        if pkeys[pygame.K_d] and self.posx + self.sizex + 5 < screenWidth:
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
    
    def gravity(self):
        # Jumping feature already pulls the player down if in jump so this runs only if player is not in jump
        if not self.isJump:
            if self.posy + self.sizey < platform.posy:
                self.posy += Gravity
            # If the player glitches and his position is below the platform this puts him on top of it
            if self.posy + self.sizey > platform.posy:
                self.posy = platform.posy - self.sizey
            self.rect.topleft = (round(self.posx), round(self.posy))

    def display(self):
        #pygame.draw.rect(screen, Blue, self.rect)
        screen.blit(self.image, self.rect)


White = (255, 255, 255)
Gray = (50, 50, 50)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
screenWidth, screenHeight = 800, 600
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

Gravity = 15     # How fast the player falls (how fast is the player pulled to the ground)

platform = Platform()
player = Player()

# ROCK DEMO
sheet = SpriteSheet()
rock = sheet.get_image('rock', scale=(32,31))
# ROCK DEMO

running = True
while running:
    clock.tick(30)
    # If no delay the game moves too fast
    pygame.time.delay(30)
    screen.fill(Gray)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    player.move(keys)
    player.gravity()

    # ROCK DEMO
    for x in range(0, 640, 32):
        screen.blit(rock, (x, 350)) 
    # ROCK DEMO

    platform.display()
    player.display()
    pygame.display.flip()

pygame.quit()
    
