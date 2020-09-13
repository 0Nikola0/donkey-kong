import pygame,time,os
from pygame.locals import *


pygame.init()


SCREENWIDTH = 800
SCREENHEIGHT = 600
FPS = 30
icon  = pygame.image.load("icon.jpg")
icon = pygame.transform.scale(icon, (70, 70))
pygame.display.set_icon(icon)
win = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("Donkey Kong Game")


Font = pygame.font.Font("Aldrich-Regular.ttf",30)
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg, (800, 600))
title = pygame.image.load("title.jpg")
title = pygame.transform.scale(title, (300, 400))

clock = pygame.time.Clock()


class mainmenubuttons(object):
    def __init__(self,name,x,y,width,height,shift):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.image =pygame.image.load("button.png")
        self.textShift = shift
    def update(self,mouseX,mouseY):
        mouserect = pygame.Rect(mouseX,mouseY,10,10)
        if self.rect.colliderect(mouserect):
            self.image =pygame.image.load("button_pressed.png")
        else:
            self.image =pygame.image.load("button.png")
    def click(self,mouseX,mouseY):
        mouserect = pygame.Rect(mouseX,mouseY,10,10)
        if self.rect.colliderect(mouserect):
            if self.name.upper() == "PLAY":
                print("play button pressed")
                # stuff to do after the button is clicked
            if self.name.upper() == "HELP":
                print("help button pressed")
                # stuff to do after the button is clicked
            if self.name.upper() == "ABOUT":
                print("about button pressed")
                # stuff to do after the button is clicked
            if self.name.upper() == "EXIT":
                pygame.quit() #added code to exit
                os._exit(1)
def main():
    run = True
    
    buttons = [mainmenubuttons("Play",300,320,200,50,70),
                mainmenubuttons("Help",300,380,200,50,40),
                mainmenubuttons("About",300,440,200,50,40),
                mainmenubuttons("Exit",300,500,200,50,70)]

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
               
                pygame.quit()
                os._exit(1)
   
        mousePos = pygame.mouse.get_pos()

        pressed1,pressed2,pressed3 = pygame.mouse.get_pressed()
        if pressed1:
            for button in buttons:
                button.click(mousePos[0],mousePos[1])
        
        win.blit(bg,(0,0))
        win.blit(title,(0,0))
        
        for button in buttons:
            
            button.update(mousePos[0],mousePos[1])
            win.blit(button.image, (button.x, button.y))
            
            text = Font.render(button.name,1,(255,255,255))
            
            win.blit(text,(button.x+button.textShift,button.y+15))
        
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
