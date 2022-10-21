
import engine.UI.Button
import engine.game_engine
from engine.UI import MainMenu,trainUI

class UI():
    
    def __init__(self,pFuncs):
        self.parentFuncs=pFuncs
        self.active=False
        self.activeUI=[]
        self.activeUI.append(trainUI.TrainUI(self))
        #self.activeUI.append(MainMenu.MainMenu(self))

    def render(self,screen):
        #Rendering the active UI
        if self.activeUI[0].active==True:
            self.activeUI[0].render(screen)

    #Checks if a button of the current ui is pressed
    def checkButtonPressed(self,type):
        if type=="MOUSEDOWN":
            return self.activeUI[0].buttonFunc()
        if type=="MOUSEUP":
            return self.activeUI[0].clickUP()

    def isActive(self):
        return self.active

    #Calls reorganizeAll function of the current actived UI
    def reorganizeAll(self):
        self.activeUI[0].reOrganizeAll()