import pygame as pg
from engine import train,object,map_load,camera
from engine.UI import UIManager
import engine.multiplayer.connection
import time,threading

colliders=[]

class gameEngine():
    def __init__(self,debug):
        self.camera = camera.Camera()
        self.train = train.TrainObject("Train",["objects","complete_train.png"],-500,100)
        self.trains = pg.sprite.RenderPlain()
        self.gameObjs = [pg.sprite.RenderPlain(),pg.sprite.RenderPlain(),pg.sprite.RenderPlain()]
        self.map=map_load.mapLoad()
        #MPTest, making mptrain list and we start the mp constructor
        #self.mpTrains={}
        #self.mp=engine.multiplayer.connection.connection(self.mpTrains,self.camera)
        #printInfo=threading.Thread(target=self.mpTrainList)
        #printInfo.start()
        self.running = True
        self.debug=debug
        self.mpTrains = None
        if(debug):
            self.font = pg.font.SysFont("font1", 24)
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
        self.section=0
        #self.uiManager=UIManager.UI(self)

    def isRunning(self):
        return self.running
    
    def mpTrainList(self):
        while self.running:
            print("MPTrains: ", self.mpTrains)
            for train in self.mpTrains.values():
                print(train.getCoords())
            time.sleep(3)

    def checkSectionChange(self):
        if self.camera.getCords()[0]>pg.display.get_window_size()[0]*self.section:
            return 1
        elif self.camera.getCords()[0]<(pg.display.get_window_size()[0]*self.section)-pg.display.get_window_size()[0]:
            return -1
        else:
            return 0

    def renderObjects(self,screen,clockFPS):
        
        self.camera.update()
        #Multiplayer Update in progress
        #for train in self.mpTrains.values():
        #    screen.blit(train.image,train.getCoords())
        #    userTagID = self.font.render(train.getName(), True, (255, 255, 0))
        #    screen.blit(userTagID, (train.getCoords()[0], train.getCoords()[1]))
        
        # POSIBLE VISIBLE SECTION 0
        self.gameObjs[0].draw(screen)
        self.gameObjs[0].update(self.camera.getCords())
        # VISIBLE SECTION 1
        self.gameObjs[1].draw(screen)
        self.gameObjs[1].update(self.camera.getCords())
        # POSIBLE VISIBLE SECTION 2
        self.gameObjs[2].draw(screen)
        self.gameObjs[2].update(self.camera.getCords())
        #Draw train
        self.trains.draw(screen)
        self.trains.update()
        #Draws debug info if Debugging mode is enabled
        if(self.debug):
            fps_count = self.font.render('FPS: '+str(clockFPS), True, (0, 255, 0))
            screen.blit(fps_count, (20, 20))
            train_speed = self.font.render(' Train Speed: '+str(self.camera.getSpeed()), True, (0, 255, 0))
            screen.blit(train_speed, (15, 50))
            current_section = self.font.render(' Section: '+str(self.section)+ ' Camera coords: '+str(self.camera.getCords()[0])+ ', '+str(self.camera.getCords()[1]), True, (0, 255, 0))
            screen.blit(current_section, (15, 70))
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
            self.gameObjs.pop(2)
            self.gameObjs.append(pg.sprite.RenderPlain())
            for i in self.map.getMapObjects(self.section-1):
                self.gameObjs[0].add(i)
        #self.uiManager.render(screen)

    def keyEventsCheck(self):
        #Keyboard events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.camera.decreaseSpeed()
                if event.key == pg.K_d:
                    self.camera.increaseSpeed()
            #Mouse event
            #if self.uiManager.isActive() == True and event.type == pg.MOUSEBUTTONUP:
            #    print(self.uiManager.checkButtonPressed())    
            #Screen resize event
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
