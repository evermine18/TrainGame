import engine.object
import os

def mapRead():
    parsedObjects=[]
    # Open the file to get the data
    with open(os.path.join("engine","map","map1.map"),'r') as data_map:
        # We need to parse the data to load into a var 
        for line in data_map:
            objects = line.split(",")
            for object in objects:
                parsedObjects.append(object.split(":"))
    # Returns a list of a lists of objects
    # Format [["objectname",x,y],...]
    return parsedObjects

class mapLoad():

    def __init__(self):
        self.mapDefs=mapDefinitions()   # Definition load
        self.objectList=mapRead()    # Map load
        self.loadedMap=[]
        # Prepare every object into loadedMap for when the engine asks for it
        for obj in self.objectList:
            self.loadedMap.append(engine.object.Object(obj[0],self.mapDefs.getDir(obj[0]),(int(obj[1]),int(obj[2])),self.mapDefs.getScale(obj[0])))
        
    def getMapObjects(self):
        return self.loadedMap

class mapDefinitions():

    def __init__(self):
        self.mapDefs={
            "Tree":[["objects","tree.png"],(140, 250)],
            "Bush":[["objects","bush1.png"],(100, 100)]}
    
    # Returns a list of a sprite dir of the requested object
    def getDir(self,name):
        if (name in self.mapDefs):
            return self.mapDefs[name][0]
        else:
            return ["objects","test.png"]
    def getScale(self,name):
        if (name in self.mapDefs):
            return self.mapDefs[name][1]
        else:
            return [100,100]