import pygame as pg

class Camera(pg.sprite.Sprite):
    def __init__(self):
        self.x=0
        self.y=0
        self.speed=0
    
    def moveCamera(self,x,y):
        self.x=x
        self.y=y
    
    def getCords(self):
        return (self.x,self.y)

    def getSpeed(self):
        return self.speed

    def increaseSpeed(self):
        self.speed+=1

    def decreaseSpeed(self):
        self.speed-=1

    def update(self):
        self.x = self.x + self.speed