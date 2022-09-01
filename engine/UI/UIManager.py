
import engine.UI.Button
import engine.game_engine
import engine.UI.MainMenu

class UI():
    
    def __init__(self,pFuncs):
        self.parentFuncs=pFuncs
        self.mainmenu=engine.UI.MainMenu.MainMenu()

    def render(self,screen):
        self.mainmenu.render(screen)
    def checkButtonPressed(self):
        return self.mainmenu.buttonFunc()