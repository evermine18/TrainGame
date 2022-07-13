from re import X
import pygame as pg
import os

colliders=[]

class GameObject(pg.sprite.Sprite):

    def __init__(self,name,sprite_dir,x=0,y=0):
        super(GameObject,self).__init__()
        self.name=name
        self.x=x
        self.y=y
        self.speed=0
        self.image=pg.image.load(os.path.join("sprites",sprite_dir[0],sprite_dir[1]))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def getCoords(self):
        print("Coords from gameObject ",self.name," x=",self.x," y=",self.y)

    def getSpeed(self):
        return self.speed

    def increaseSpeed(self):
        self.speed+=1

    def decreaseSpeed(self):
        self.speed-=1

    def getRenderObj(self):
        return self.renderObj

    def update(self):
        self.rect.x = self.rect.x + self.speed


    
