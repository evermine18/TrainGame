from turtle import speed
import pygame as pg
import os

class TrainObject(pg.sprite.Sprite):

    def __init__(self,name,sprite_dir,x=0,y=0):
        super(TrainObject,self).__init__()
        self.name=name
        self.x=x
        self.y=y
        self.route=0
        self.speed=0
        self.image=pg.image.load(os.path.join("sprites",sprite_dir[0],sprite_dir[1]))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def getCoords(self):
        return (self.rect.x,self.rect.y)

    def getSpeed(self):
        return self.speed

    def getName(self):
        return self.name

    def getCurrentPos(self):
        return int(self.route)
        
    def increaseSpeed(self):
        self.speed+=1

    def decreaseSpeed(self):
        self.speed-=1
    
    def updateCords(self,xpos):
        #print("xpos es:",xpos)
        self.rect.x=xpos
    def update(self):
        #old train code, not used
        #self.rect.x = self.rect.x + self.speed
        #self.route+=self.speed
        self.rect.y = pg.display.get_window_size()[1]-self.y
        pass