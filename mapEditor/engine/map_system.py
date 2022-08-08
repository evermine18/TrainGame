import engine.object
import os

def mapRead():
    parsedObjects=[]
    # Open the file to get the data
    with open(os.path.join("mapEditor","engine","map","map1.map"),'r') as data_map:
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
        self.objectList=[]
        self.loadedMap=[]
    def addObject(self,object):
        self.objectList.append(object)
    def getMapObjects(self):
        for obj in self.objectList:
            self.loadedMap.append(engine.object.Object(obj[0],self.mapDefs.getDir(obj[0]),(int(obj[1]),int(obj[2])),self.mapDefs.getScale(obj[0])))
        return self.loadedMap
    def getObjectList(self):
        return self.objectList
    def saveMap(self):
        mapData=""
        for i in self.objectList:
            mapData+=str(i[0])+":"
            mapData+=str(i[1])+":"
            mapData+=str(i[2])+","
        with open(os.path.join("mapEditor","engine","map","map1.map"),'w') as file:
            file.write(mapData[0:len(mapData)-1])

class mapDefinitions():

    def __init__(self):
        self.mapDefs={
            "1":[["objects","tree.png"],(140, 250)],
            "2":[["objects","bush1.png"],(100, 100)]}
    
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