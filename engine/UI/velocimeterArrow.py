import pygame as pg

import os

class Arrow(pg.sprite.Sprite):
    def __init__(self,sprite_dir,funcID,coords=(0,0),scale=(100,100)):
        super(Arrow,self).__init__()
        self.orgImage=pg.image.load(os.path.join("engine","UI","UISprites",sprite_dir[0],sprite_dir[1])).convert_alpha()
        self.orgImage=pg.transform.scale(self.orgImage, scale)
        self.image=self.orgImage
        self.image=pg.transform.rotate(self.image,120)
        self.scale = scale
        self.coords=coords
        self.rect = self.image.get_rect()
        self.rect.center = coords
    
    def setCoords(self,coords):
        self.rect = pg.Rect(coords[0],coords[1],self.scale[0],self.scale[1])

    def setX(self,x):
        self.rect= pg.Rect(x,self.rect.y,self.scale[0],self.scale[1])

    def rotate(self,value):
        self.image=pg.transform.rotate(self.orgImage,120-value)

    def update(self,pos):
        self.rect.center = pos