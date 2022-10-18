import engine.UI.Button
import pygame as pg
import os

class MainMenu():
    def __init__(self,UIManager):
        UIManager.active=True
        self.active=True
        self.buttons=pg.sprite.RenderPlain()
        self.buttons.add(engine.UI.Button.Button(("Buttons","button_1.png"),1,(100,100),(134,32)))
        #self.playButton=engine.UI.Button.Button(("Buttons","button_1.png"),(100,100),(134,32))
        self.font = pg.font.Font(os.path.join("engine","UI","UIFonts","VT323-Regular.ttf"), 24)


    def render(self,screen):
        pg.draw.rect(screen, (255,255,255), pg.Rect(0, 0, pg.display.get_window_size()[0], pg.display.get_window_size()[1]))
        self.buttons.draw(screen)
        #screen.blit(self.playButton,self.playButton.getCords())
        play_text = self.font.render('Play',True, (255, 255, 255))
        screen.blit(play_text, (70, 84))
        
    
    def buttonFunc(self):
        funcID=0
        for sprite in self.buttons:
            if sprite.getCords()[0]<pg.mouse.get_pos()[0] and sprite.getCords()[1]<pg.mouse.get_pos()[1]:
                if (sprite.getCords()[0]+sprite.getScale()[0])>pg.mouse.get_pos()[0] and (sprite.getCords()[1]+sprite.getScale()[1])>pg.mouse.get_pos()[1]:
                    funcID=sprite.getFuncID()

        if funcID==1:
            self.active=False
