
import pygame as pg
import os


class Traffic_lights(pg.sprite.Sprite):
    
    def __init__(self,name,sprite_dir,coords=(0,0),scale=(100,100)):
        super(Traffic_lights,self).__init__()
        self.name=name
        self.image=pg.image.load(os.path.join("sprites",sprite_dir[0],sprite_dir[1]))
        self.image=pg.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.x=self.rect.x
        self.y=self.rect.y
        self.state="green"
        self.timer=0
        print("semaforo")

    def getCoords(self):
        print("Coords from gameObject ",self.name," x=",self.x," y=",self.y)
    
    def update(self,cameraCords):
        self.rect.x=(cameraCords[0]*-1)+self.x
        if cameraCords[0]==self.x-170:
            print("sisisisiisis")
            self.image=pg.image.load(os.path.join("sprites","objects","traffic_light_red.png"))
            self.image=pg.transform.scale(self.image, (38, 100))
            self.state="red"
        if self.state=="red":
            self.timer+=0.01
            if self.timer>10:
                self.image=pg.image.load(os.path.join("sprites","objects","traffic_light_yellow.png"))
                self.image=pg.transform.scale(self.image, (38, 100))
                self.timer=0
                self.state="yellow"
        if self.state=="yellow":
            self.timer+=0.01
            if self.timer>10:
                self.image=pg.image.load(os.path.join("sprites","objects","traffic_light_green.png"))
                self.image=pg.transform.scale(self.image, (38, 100))
                self.timer=0
                self.state="green"
        #print(self.rect.x)
        #self.rect.y=self.train.y-self.y
