
import engine.UI.Button
import engine.game_engine
import engine.UI.MainMenu

class UI():
    
    def __init__(self,pFuncs):
        self.parentFuncs=pFuncs
        self.active=False
        self.mainmenu=engine.UI.MainMenu.MainMenu(self)

    def render(self,screen):
        #Rendering the active UI
        if self.mainmenu.active==True:
            self.mainmenu.render(screen)

    #Checks if a button of the current ui is pressed
    def checkButtonPressed(self):
        return self.mainmenu.buttonFunc()

    def isActive(self):
        return self.active

    #Calls reorganizeAll function of the current actived UI
    def reorganizeAll(self):
        self.mainmenu.reOrganizeAll()