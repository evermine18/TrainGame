import pygame as pg
from engine.UI import Button, image
from engine import game_engine,camera


class TrainUI():
    def __init__(self,UIManager):
        UIManager.active=True
        self.active=True
        self.images=pg.sprite.RenderPlain()
        self.limiterPanel=image.Image(("Images","speedLimiter.png"),1,(pg.display.get_window_size()[0]-40,140),(50,218))
        self.limiterPanel.setCoords((pg.display.get_window_size()[0]-70,30))
        self.speedLimiter=image.Image(("Images","trainUI.png"),1,(pg.display.get_window_size()[0]/2,200),(53,25))
        self.speedLimiter.setCoords((pg.display.get_window_size()[0]-95,self.speedLimiter.rect.y))
        self.drag=False
    
    def render(self,screen):
        #self.images.draw(screen)
        screen.blit(self.limiterPanel.image,(self.limiterPanel.rect.x,self.limiterPanel.rect.y))
        screen.blit(self.speedLimiter.image,(self.speedLimiter.rect.x,self.speedLimiter.rect.y))
        if self.drag==True:
            x, y = pg.mouse.get_pos()
            if y>30 and y<230:
                self.speedLimiter.setCoords((pg.display.get_window_size()[0]-95,y))
                camera.Camera.wantedSpeed=round((185-y)/20)
                print(camera.Camera.wantedSpeed)


    def buttonFunc(self):
        #Change this with screen blit
        x, y = pg.mouse.get_pos()
        if self.speedLimiter.rect.collidepoint(x, y):
            self.drag=True
            
    def clickUP(self):
        self.drag=False
    def reOrganizeAll(self):
        for sprite in self.images:
            sprite.setX((pg.display.get_window_size()[0]-100))
        self.limiterPanel.setCoords((pg.display.get_window_size()[0]-70,30))
        self.speedLimiter.setCoords((pg.display.get_window_size()[0]-95,self.speedLimiter.rect.y))