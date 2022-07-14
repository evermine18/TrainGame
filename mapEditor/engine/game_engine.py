from distutils.log import debug
from re import X
import pygame as pg
import engine.train,engine.object,engine.posibleObject,engine.map_system

colliders=[]

class gameEngine():
    def __init__(self,debug):
        self.train = engine.train.TrainObject("Train",["objects","complete_train.png"],1000,450)
        self.gameObjs = pg.sprite.RenderPlain()
        self.map=engine.map_system.mapLoad()
        self.mapDefs=engine.map_system.mapDefinitions()
        self.pObject = engine.posibleObject.Object("Unknown",self.mapDefs.getDir("1"),(300,450),self.mapDefs.getScale("1"))
        self.running = True
        self.debug=debug
        if(debug):
            self.font = pg.font.SysFont(None, 24)
        #self.tree = engine.object.Object("Tree",["objects","tree.png"],100,380)
        #self.gameObjs.add(self.tree)
        for i in self.map.getMapObjects():
            self.gameObjs.add(i)
        self.gameObjs.add(self.pObject)
        self.gameObjs.add(self.train)

    def isRunning(self):
        return self.running

    def renderObjects(self,screen,clockFPS):
        x, y=pg.mouse.get_pos()
        self.pObject.setCords(x,y)
        self.gameObjs.draw(screen)
        self.gameObjs.update()
        #Draws debug info if Debugging mode is enabled
        if(self.debug):
            fps_count = self.font.render('FPS: '+str(clockFPS), True, (0, 255, 0))
            screen.blit(fps_count, (20, 20))
            train_speed = self.font.render(' Train Speed: '+str(self.train.getSpeed()), True, (0, 255, 0))
            screen.blit(train_speed, (15, 50))
    
    def keyEventsCheck(self):
        #Keyboard events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    self.train.increaseSpeed()
                if event.key == pg.K_a:
                    self.train.decreaseSpeed()
                if event.key == pg.K_RIGHT:
                    self.pObject.nextObject()
                if event.key == pg.K_LEFT:
                    self.pObject.lastObject()
                if event.key == pg.K_o:
                    self.map.saveMap()
                    print("SAVED MAP!!")
            if event.type == pg.MOUSEBUTTONUP:
                self.map.addObject(self.pObject.getObjectDetails())
                self.gameObjs.empty()
                for i in self.map.getMapObjects():
                    self.gameObjs.add(i)
                self.gameObjs.add(self.pObject)
                self.gameObjs.add(self.train)

    
