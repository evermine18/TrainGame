from distutils.log import debug
from re import X
import pygame as pg
import engine.train,engine.object,engine.posibleObject,engine.map_system,engine.camera

colliders=[]

class gameEngine():
    def __init__(self,debug):
        self.camera = engine.camera.Camera()
        self.train = engine.train.TrainObject("Train",["objects","complete_train.png"],1000,450)
        self.trains = pg.sprite.RenderPlain()
        self.pObjects = pg.sprite.RenderPlain()
        self.gameObjs = [pg.sprite.RenderPlain(),pg.sprite.RenderPlain(),pg.sprite.RenderPlain()]
        self.map=engine.map_system.mapLoad()
        self.mapDefs=engine.map_system.mapDefinitions()
        self.pObject = engine.posibleObject.Object("Unknown",self.mapDefs.getDir("1"),(300,450),self.mapDefs.getScale("1"))
        self.running = True
        self.debug=debug
        if(debug):
            self.font = pg.font.SysFont(None, 24)
        #self.tree = engine.object.Object("Tree",["objects","tree.png"],100,380)
        #self.gameObjs.add(self.tree)
        #This loads the 3 first sections (-1,0,1)
        for i in self.map.getMapObjects(-1):
            self.gameObjs[0].add(i)
        for i in self.map.getMapObjects(0):
            self.gameObjs[1].add(i)
        for i in self.map.getMapObjects(1):
            self.gameObjs[2].add(i)
        self.trains.add(self.train)
        self.pObjects.add(self.pObject)
        self.section=0

    def checkSectionChange(self):
        if self.camera.getCords()[0]>pg.display.get_window_size()[0]*self.section:
            return 1
        elif self.camera.getCords()[0]<(pg.display.get_window_size()[0]*self.section)-pg.display.get_window_size()[0]:
            return -1
        else:
            return 0
    
    def isRunning(self):
        return self.running

    def renderObjects(self,screen,clockFPS):
        self.camera.update()
        x, y=pg.mouse.get_pos()
        self.pObjects.draw(screen)
        #self.trains.draw(screen)
        #self.trains.update()
        self.pObject.setCords(x,y)
        # POSIBLE VISIBLE SECTION 0
        self.gameObjs[0].draw(screen)
        self.gameObjs[0].update(self.camera.getCords())
        # VISIBLE SECTION 1
        self.gameObjs[1].draw(screen)
        self.gameObjs[1].update(self.camera.getCords())
        # POSIBLE VISIBLE SECTION 2
        self.gameObjs[2].draw(screen)
        self.gameObjs[2].update(self.camera.getCords())
        self.pObjects.update()
        #Draws debug info if Debugging mode is enabled
        if(self.debug):
            fps_count = self.font.render('FPS: '+str(clockFPS), True, (0, 255, 0))
            screen.blit(fps_count, (20, 20))
            train_speed = self.font.render(' Camera Speed: '+str(self.camera.getSpeed()), True, (0, 255, 0))
            screen.blit(train_speed, (15, 50))
            train_speed = self.font.render(' Train Coords: '+str(self.train.getCoords())+"Mouse: "+str(x)+", "+str(y), True, (0, 255, 0))
            screen.blit(train_speed, (15, 80))
        # TODO 
        # Make a other function for conditions and game checks or map loads
        if self.checkSectionChange()==1:
            print("Load next section")
            self.section+=1
            self.gameObjs.pop(0)
            self.gameObjs.append(pg.sprite.RenderPlain())
            for i in self.map.getMapObjects(self.section+1):
                self.gameObjs[2].add(i)
        elif self.checkSectionChange()==-1:
            print("Load last section")
            self.section-=1
            self.gameObjs.pop(0)
            self.gameObjs.append(pg.sprite.RenderPlain())
            for i in self.map.getMapObjects(self.section-1):
                self.gameObjs[0].add(i)
    
    def keyEventsCheck(self):
        #Keyboard events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    self.camera.decreaseSpeed()
                if event.key == pg.K_a:
                    self.camera.increaseSpeed()
                if event.key == pg.K_RIGHT:
                    self.pObject.nextObject()
                if event.key == pg.K_LEFT:
                    self.pObject.lastObject()
                if event.key == pg.K_o:
                    self.map.saveMap()
                    print("Info: Map saved on /mapEditor/engine/map/map1.map")
                if event.key == pg.K_l:
                    print(self.map.getObjectList())
            if event.type == pg.MOUSEBUTTONUP:
                print("New Object x=",self.pObject.getCoords()[0],"y=",self.pObject.getCoords()[1])
                self.map.addObject(self.pObject.getObjectDetails(self.camera.getCords(),pg.display.get_window_size()))
                self.gameObjs[0].empty()
                self.gameObjs[1].empty()
                self.gameObjs[2].empty()
                for i in self.map.getMapObjects(self.section-1):
                    self.gameObjs[0].add(i)
                for i in self.map.getMapObjects(self.section):
                    self.gameObjs[1].add(i)
                for i in self.map.getMapObjects(self.section+1):
                    self.gameObjs[2].add(i)
                #self.gameObjs.add(self.pObject)
                #self.gameObjs.add(self.train)
            if event.type==pg.VIDEORESIZE:
                print("si")
                self.gameObjs.clear()
                self.gameObjs=[pg.sprite.RenderPlain(),pg.sprite.RenderPlain(),pg.sprite.RenderPlain()]
                for i in self.map.getMapObjects(self.section-1):
                    self.gameObjs[0].add(i)
                for i in self.map.getMapObjects(self.section):
                    self.gameObjs[1].add(i)
                for i in self.map.getMapObjects(self.section+1):
                    self.gameObjs[2].add(i)

            

    
