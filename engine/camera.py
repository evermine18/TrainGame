import pygame as pg

class Camera(pg.sprite.Sprite):

    wantedSpeed=0

    def __init__(self):
        self.x=0
        self.y=0
        self.speed=0
        self.wspeed=0
    
    def moveCamera(self,x,y):
        self.x=x
        self.y=y
    
    def getCords(self):
        return (round(self.x),self.y)

    def getSpeed(self):
        return self.speed

    def increaseSpeed(self):
        self.wspeed+=1

    def decreaseSpeed(self):
        self.wspeed-=1

    def update(self):
        self.x = self.x + self.speed
        self.wspeed = Camera.wantedSpeed
        #print(Camera().wantedSpeed)
        if self.wspeed>self.speed:
            self.speed+=0.005
            if self.wspeed<self.speed:
                self.speed=round(self.speed)
        elif self.wspeed<self.speed:
            self.speed-=0.01
            if self.wspeed>self.speed:
                self.speed=round(self.speed)