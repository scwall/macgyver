import os
class LoadMap:

    # Create variables for instance
    def __init__(self, level=1):
        self.mapList = []
        self.level = level
        self.mapRead = str()

    # Read map in folder maps and choice of map
    def readFolderMap(self):
        levelMap = "maps/level" + str(self.level)
        with open(levelMap, "r") as map:
            self.mapRead = map.read()

    #Create list on two level
    def createMapList(self):
        listBuild = []
        for level in self.mapRead:
            if level is "\n":
                self.mapList.append(listBuild[:])
                listBuild = []
            else:
                listBuild.append(level)

    #Return of a list in encapsulation
    @property
    def getMap(self):
        return self.mapList


