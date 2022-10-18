import pygame as pg
import os

class Button(pg.sprite.Sprite):
    
    def __init__(self,sprite_dir,funcID,coords=(0,0),scale=(100,100)):
        super(Button,self).__init__()
        self.image=pg.image.load(os.path.join("engine","UI","UISprites",sprite_dir[0],sprite_dir[1])).convert_alpha()
        self.image=pg.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.coords = coords
        self.rect.center = (round(pg.display.get_window_size()[0]/2)+coords[0],round(pg.display.get_window_size()[1]/2)+coords[1])
        self.funcID=funcID
    
    def getCords(self):
        return (self.rect.x,self.rect.y)

    def getFuncID(self):
        return self.funcID
    
    def getScale(self):
        print(self.image.get_size())
        return self.image.get_size()

    def update(self):
        self.rect.center = (round(pg.display.get_window_size()[0]/2)+self.coords[0],round(pg.display.get_window_size()[1]/2)+self.coords[1])