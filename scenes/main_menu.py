import pygame
import settings as s

pygame.init()

IMGS_PATH = "../resources/images/menu_stuff/"
FONTS_PATH = "../resources/fonts/"
icon = pygame.image.load(IMGS_PATH + "icon.jpg")
icon = pygame.transform.scale(icon, (70, 70))
screen = pygame.display.set_mode(s.SCREEN_SIZE)
pygame.display.set_icon(icon)
pygame.display.set_caption("Donkey Kong Game")

Font = pygame.font.Font(FONTS_PATH + "Aldrich-Regular.ttf", 30)
bg = pygame.image.load(IMGS_PATH + "bg.jpg")
bg = pygame.transform.scale(bg, (800, 600))
title = pygame.image.load(IMGS_PATH + "title.jpg")
title = pygame.transform.scale(title, (300, 400))

clock = pygame.time.Clock()


class MainMenuButton(object):
    def __init__(self, name, pos, size):
        self.name = name    # Used only to print which button is clicked, probably wont be needed later
        self.text = Font.render(self.name, True, s.WHITE)
        self.text_pos = self.text.get_rect()
        self.text_pos.center = pos

        self.posx, self.posy = pos
        self.width, self.height = size
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.rect.center = pos

        self.image_idle = pygame.image.load(IMGS_PATH + "button.png")
        self.image_idle = pygame.transform.scale(self.image_idle, (self.width, self.height))

        self.image_pressed = pygame.image.load(IMGS_PATH + "button_pressed.png")
        self.image_pressed = pygame.transform.scale(self.image_pressed, (self.width + 5, self.height))

        self.image = self.image_idle

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            self.image = self.image_pressed
        else:
            self.image = self.image_idle

    def click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
            print("Pressed: " + self.name)
            # Need to fix this later
            if self.text.upper() == "EXIT":
                pygame.quit()  # added code to exit

    def display(self):
        screen.blit(self.image, (self.rect.x, self.rect.y - 2))
        screen.blit(self.text, self.text_pos)


def main():
    bpx = 670   # Button pos x
    bsx = 200   # Button size x
    bsy = 50
    buttons = [["Play", MainMenuButton("Play", (bpx, 320), (bsx, bsy))],
               ["Help", MainMenuButton("Help", (bpx, 380), (bsx, bsy))],
               ["About", MainMenuButton("About", (bpx, 440), (bsx, bsy))],
               ["Exit", MainMenuButton("Exit", (bpx, 500), (bsx, bsy))]]

    running = True
    while running:
        clock.tick(s.FRAME_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                running = False

        mouse_pos = pygame.mouse.get_pos()

        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        if pressed1:
            for button in buttons:
                button[1].click(mouse_pos)

        screen.blit(bg, (0, 0))
        screen.blit(title, (0, 0))

        for button in buttons:
            button[1].update(mouse_pos)
            button[1].display()

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
