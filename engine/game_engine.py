from re import X
import pygame as pg
import os

class GameObject():
    name=""
    x=0
    y=0
    renderObj=""
    def __init__(self,name,x=0,y=0):
        self.name=name
        self.x=x
        self.y=y
        self.renderObj=RenderObject(["objects","test.png"],self.x,self.y)
    def getCoords(self):
        print("Coords from gameObject ",self.name," x=",self.x," y=",self.y)
    def getRenderObj(self):
        return self.renderObj
class RenderObject(pg.sprite.Sprite):
    sprite=""
    def __init__(self,sprite_loc,x,y):
        super(RenderObject, self).__init__()
        self.image=pg.image.load(os.path.join("sprites",sprite_loc[0], sprite_loc[1]))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self):
        GameObject.getCoords()
        pass
