from engine.UI import Button, image
from engine import game_engine
import pygame as pg
import os

class MainMenu():
    def __init__(self,UIManager):
        UIManager.active=True
        self.active=True
        self.buttons=pg.sprite.RenderPlain()
        self.buttons.add(Button.Button(("Buttons","button_play.png"),1,(0,0),(134,32)))
        self.buttons.add(Button.Button(("Buttons","button_exit.png"),2,(0,40),(134,32)))
        #self.playButton=engine.UI.Button.Button(("Buttons","button_1.png"),(100,100),(134,32))
        self.font = pg.font.Font(os.path.join("engine","UI","UIFonts","VT323-Regular.ttf"), 24)
        self.images=pg.sprite.RenderPlain()
        #self.images.add(image.Image(("Images","menuBackground.png"),1,(0,0),(1920,1080)))
        self.images.add(image.Image(("Images","trainSimLogo.png"),1,(pg.display.get_window_size()[0]/2,(pg.display.get_window_size()[1]/2)-150),(500,103)))
        self.background=pg.image.load(os.path.join("engine","UI","UISprites","Images","menuBackground.png")).convert_alpha()
        self.background=pg.transform.scale(self.background, (pg.display.get_window_size()[0],pg.display.get_window_size()[1]))

    def render(self,screen):
        screen.blit(self.background,(0,0))
        #pg.draw.rect(screen, (255,255,255), pg.Rect(0, 0, pg.display.get_window_size()[0], pg.display.get_window_size()[1]))
        self.images.draw(screen)
        self.buttons.draw(screen)
        #screen.blit(self.playButton,self.playButton.getCords())
        #play_text = self.font.render('Play',True, (255, 255, 255))
        #screen.blit(play_text, ((pg.display.get_window_size()[0]/2)-20,((pg.display.get_window_size()[1]/2)-12)))

        
    
    def buttonFunc(self):
        funcID=0
        for sprite in self.buttons:
            if sprite.getCords()[0]<pg.mouse.get_pos()[0] and sprite.getCords()[1]<pg.mouse.get_pos()[1]:
                if (sprite.getCords()[0]+sprite.getScale()[0])>pg.mouse.get_pos()[0] and (sprite.getCords()[1]+sprite.getScale()[1])>pg.mouse.get_pos()[1]:
                    funcID=sprite.getFuncID()

        if funcID==1:
            self.active=False
        if funcID==2:
            game_engine.gameEngine.running=False

    def reOrganizeAll(self):
        self.background=pg.image.load(os.path.join("engine","UI","UISprites","Images","menuBackground.png")).convert_alpha()
        self.background=pg.transform.scale(self.background, (pg.display.get_window_size()[0],pg.display.get_window_size()[1]))
        self.images.update(((pg.display.get_window_size()[0]/2,(pg.display.get_window_size()[1]/2)-150)))
        self.buttons.update()