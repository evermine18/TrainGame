from re import X
import pygame as pg
import os

class GameObject():
    name=""
    x=0
    y=0
    def __init__(self,name,x=0,y=0):
        self.name=name
        self.x=x
        self.y=y
    
    def getCoords(self):
        print("Coords from gameObject ",self.name," x=",self.x," y=",self.y)
    
class RenderObject(pg.sprite.Sprite):
    sprite=""
    def __init__(self,sprite_loc,x,y):
        self.sprite=pg.image.load(os.path.join(sprite_loc[0], sprite_loc[1]))
        self.rect = self.image.get_rect()

    def update(self):
        pass
