import pygame as pg
import os
import engine.map_system

class Object(pg.sprite.Sprite):

    def __init__(self,name,sprite_dir,coords=(0,0),scale=(100,100)):
        super(Object,self).__init__()
        self.name=name
        self.id=1
        self.x=coords[0]
        self.y=coords[1]
        self.mapDef=engine.map_system.mapDefinitions()
        self.image=pg.image.load(os.path.join("sprites",self.mapDef.getDir(str(self.id))[0],self.mapDef.getDir(str(self.id))[1]))
        self.image=pg.transform.scale(self.image, self.mapDef.getScale(str(self.id)))
        print(self.image.get_rect())
        self.rect = self.image.get_rect()
        self.rect.center = coords

    def getCoords(self):
        return (self.x,self.y)

    def getObjectDetails(self,cameraCoords):
        return [str(self.id),self.x-cameraCoords[0],self.y]

    def setCords(self,x,y):
        self.x = x
        self.y = y

    def nextObject(self):
        self.id += 1
        self.image=pg.image.load(os.path.join("sprites",self.mapDef.getDir(str(self.id))[0],self.mapDef.getDir(str(self.id))[1]))
        self.image=pg.transform.scale(self.image, self.mapDef.getScale(str(self.id)))

    def lastObject(self):
        self.id -= 1
        self.image=pg.image.load(os.path.join("sprites",self.mapDef.getDir(str(self.id))[0],self.mapDef.getDir(str(self.id))[1]))
        self.image=pg.transform.scale(self.image, self.mapDef.getScale(str(self.id)))

    def update(self):
        self.rect.x = self.x - self.mapDef.getScale(str(self.id))[0]/2
        self.rect.y = self.y - self.mapDef.getScale(str(self.id))[1]/2
