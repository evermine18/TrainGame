import pygame as pg
from engine.UI import Button, image
from engine import game_engine


class TrainUI():
    def __init__(self,UIManager):
        UIManager.active=True
        self.active=True
        self.images=pg.sprite.RenderPlain()
        self.images.add(image.Image(("Images","trainUI.png"),1,(pg.display.get_window_size()[0]/2,(pg.display.get_window_size()[1]/2)-150),(21,15)))
        self.drag=False
    
    def render(self,screen):
        self.images.draw(screen)
        if self.drag==True:
            x, y = pg.mouse.get_pos()
            for sprite in self.images:
                sprite.setCoords((x, y))


    def buttonFunc(self):
        #Change this with screen blit
        x, y = pg.mouse.get_pos()
        
        for sprite in self.images:
            if sprite.rect.collidepoint(x, y):
                self.drag=True
    def clickUP(self):
        self.drag=False
    def reOrganizeAll(self):
        pass