import engine.UI.Button
import pygame as pg
import os

class MainMenu():
    def __init__(self):
        
        self.buttons=pg.sprite.RenderPlain()
        self.buttons.add(engine.UI.Button.Button(("Buttons","button_1.png"),1,(100,100),(134,32)))
        #self.playButton=engine.UI.Button.Button(("Buttons","button_1.png"),(100,100),(134,32))
        self.font = pg.font.Font(os.path.join("engine","UI","UIFonts","VT323-Regular.ttf"), 24)
    def render(self,screen):
        self.buttons.draw(screen)
        #screen.blit(self.playButton,self.playButton.getCords())
        play_text = self.font.render('Play',True, (255, 255, 255))
        screen.blit(play_text, (70, 84))
    
    def buttonFunc(self):
        for sprite in self.buttons:
            if sprite.getCords()[0]<pg.mouse.get_pos()[0] and sprite.getCords()[1]<pg.mouse.get_pos()[1]:
                if (sprite.getCords()[0]+sprite.getScale()[0])>pg.mouse.get_pos()[0] and (sprite.getCords()[1]+sprite.getScale()[1])>pg.mouse.get_pos()[1]:
                    return sprite.getFuncID()

        
