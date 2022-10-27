
import engine.UI.Button
import engine.game_engine
from engine.UI import MainMenu,trainUI

class UI():
    
    def __init__(self,pFuncs):
        self.parentFuncs=pFuncs
        self.active=False
        self.activeUI=[]
        #self.activeUI.append(MainMenu.MainMenu(self))
        self.activeUI.append(trainUI.TrainUI(self))

    def render(self,screen):
        #Rendering the active UI
        for i in range(len(self.activeUI)-1,-1,-1):
            if self.activeUI[i].active==True:
                self.activeUI[i].render(screen)

    #Checks if a button of the current ui is pressed
    def checkButtonPressed(self,type):
        for i in range(len(self.activeUI)-1,-1,-1):
            if type=="MOUSEDOWN":
                return self.activeUI[i].buttonFunc()
            if type=="MOUSEUP":
                return self.activeUI[i].clickUP()

    def isActive(self):
        return self.active

    def updateUI(self,value):
        for i in range(len(self.activeUI)-1,-1,-1):
            self.activeUI[i].updateUI(value)

    #Calls reorganizeAll function of the current actived UI
    def reorganizeAll(self):
        for i in range(len(self.activeUI)-1,-1,-1):
            self.activeUI[i].reOrganizeAll()