from email.mime import image
import pygame as pg
import os
import engine.map_system

class Object(pg.sprite.Sprite):

    def __init__(self,name,sprite_dir,coords=(0,0),scale=(100,100)):
        super(Object,self).__init__()
        self.name=name
        self.mapDef=engine.map_system.mapDefinitions()
        self.image=pg.image.load(os.path.join("sprites",sprite_dir[0],sprite_dir[1])).convert_alpha()
        self.image=pg.transform.scale(self.image, scale)
        print(self.image.get_rect())
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.x=self.rect.x
        self.y=self.rect.y
        print("Coords:",self.x)
        print("Coords:",self.rect.x)

    def getCoords(self):
        print("Coords from gameObject ",self.name," x=",self.x," y=",self.y)

    def update(self,cameraCoords):
        #print(trainX.getCurrentPos())
        self.rect.x=cameraCoords[0]+self.x
        #self.rect.x=(self.x-self.mapDef.getScale(str(0))[0]/2)
        #print(self.rect.x)
        #self.rect.y=self.train.y-self.y
