
import pygame as pg
import os

class Object(pg.sprite.Sprite):

    def __init__(self,name,sprite_dir,coords=(0,0),scale=(100,100)):
        super(Object,self).__init__()
        self.name=name
        self.image=pg.image.load(os.path.join("sprites",sprite_dir[0],sprite_dir[1])).convert_alpha()
        self.image=pg.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.x=self.rect.x
        self.y=self.rect.y

    def getCoords(self):
        print("Coords from gameObject ",self.name," x=",self.x," y=",self.y)
    
    def update(self,cameraCords):
        self.rect.x=cameraCords[0]+self.x
        #print(self.rect.x)
        #self.rect.y=self.train.y-self.y
