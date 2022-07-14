from email.mime import image
import pygame as pg
import os

class Object(pg.sprite.Sprite):

    def __init__(self,name,sprite_dir,coords=(0,0),scale=(100,100)):
        super(Object,self).__init__()
        self.name=name
        self.x=coords[0]
        self.y=coords[1]
        self.image=pg.image.load(os.path.join("sprites",sprite_dir[0],sprite_dir[1]))
        self.image=pg.transform.scale(self.image, scale)
        print(self.image.get_rect())
        self.rect = self.image.get_rect()
        self.rect.center = coords

    def getCoords(self):
        print("Coords from gameObject ",self.name," x=",self.x," y=",self.y)

    def update(self):
        pass
