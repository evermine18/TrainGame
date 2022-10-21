from engine.UI import Button, image
from engine import game_engine
import pygame as pg
import os

class MainMenu():
    def __init__(self,UIManager):
        UIManager.active=True
        self.active=True
        #Buttons
        self.buttons=pg.sprite.RenderPlain()
        self.buttons.add(Button.Button(("Buttons","button_play.png"),1,(0,0),(134,32)))
        self.buttons.add(Button.Button(("Buttons","button_exit.png"),2,(0,40),(134,32)))
        #Fonts
        self.font = pg.font.Font(os.path.join("engine","UI","UIFonts","VT323-Regular.ttf"), 24)
        #Images
        self.images=pg.sprite.RenderPlain()
        self.images.add(image.Image(("Images","trainSimLogo.png"),1,(pg.display.get_window_size()[0]/2,(pg.display.get_window_size()[1]/2)-150),(500,103)))
        self.background=pg.image.load(os.path.join("engine","UI","UISprites","Images","menuBackground.png")).convert_alpha()
        self.background=pg.transform.scale(self.background, (pg.display.get_window_size()[0],pg.display.get_window_size()[1]))

    def render(self,screen):
        #Rendering background first
        screen.blit(self.background,(0,0))
        #Rendering all menu components
        self.images.draw(screen)
        self.buttons.draw(screen)
    
    #This function is called by a click event if the user has clicked on a button and execute the button bunction
    def buttonFunc(self):
        funcID=0
        x, y = pg.mouse.get_pos()
        #For that checks every button pos
        for sprite in self.buttons:
            if sprite.rect.collidepoint(x, y):
                funcID=sprite.getFuncID()

        if funcID==1:
            self.active=False
        if funcID==2:
            game_engine.gameEngine.running=False

    def clickUP(self):
        pass

    #Function which is responsible for readjusting everything components
    def reOrganizeAll(self):
        self.background=pg.image.load(os.path.join("engine","UI","UISprites","Images","menuBackground.png")).convert_alpha()
        self.background=pg.transform.scale(self.background, (pg.display.get_window_size()[0],pg.display.get_window_size()[1]))
        self.images.update(((pg.display.get_window_size()[0]/2,(pg.display.get_window_size()[1]/2)-150)))
        self.buttons.update()