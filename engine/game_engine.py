from re import X
import pygame as pg
import os

colliders=[]

class GameObject(pg.sprite.Sprite):
    name=""
    x=0
    y=0
    renderObj=""
    def __init__(self,name,sprite_dir,x=0,y=0):
        super(GameObject,self).__init__()
        self.name=name
        self.x=x
        self.y=y
        self.image=pg.image.load(os.path.join("sprites",sprite_dir[0],sprite_dir[1]))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def getCoords(self):
        print("Coords from gameObject ",self.name," x=",self.x," y=",self.y)
    def getRenderObj(self):
        return self.renderObj
class RenderObject(pg.sprite.Sprite):
    sprite=""
    def __init__(self,sprite_loc,x,y):
        super(self).__init__()
        self.image=pg.image.load(os.path.join("sprites",sprite_loc[0], sprite_loc[1]))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    
