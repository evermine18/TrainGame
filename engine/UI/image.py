import pygame as pg

import os

class Image(pg.sprite.Sprite):
    def __init__(self,sprite_dir,funcID,coords=(0,0),scale=(100,100)):
        super(Image,self).__init__()
        self.image=pg.image.load(os.path.join("engine","UI","UISprites",sprite_dir[0],sprite_dir[1])).convert_alpha()
        self.image=pg.transform.scale(self.image, scale)
        self.coords=coords
        self.rect = self.image.get_rect()
        self.rect.center = coords

    def update(self,pos):
        self.rect.center = pos