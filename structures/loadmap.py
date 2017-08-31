import random
import os
from structures.roadpictures import roadPictures


class LoadMap:
    # Create variables for instance
    def __init__(self, **level):
        self.mapList = []
        self.level = level["level"]
        self.mapRead = str()

    # Read map in folder maps and choice of map
    def readFolderMap(self):
        levelMap = roadPictures("maps", "level") + str(self.level)
        with open(levelMap, "r") as map:
            self.mapRead = map.read()

    # Create list on two level
    def createMapList(self):
        listBuild = []
        for level in self.mapRead:
            if level is "\n":
                self.mapList.append(list(listBuild))
                listBuild = []
            else:
                listBuild.append(level)
        self.randomObjet()

    def randomObjet(self):
        iii = 0
        while iii != len(os.listdir(os.path.join('pictures', 'artifacts'))):
            i = random.randrange(2, (len(self.mapList) - 2))
            ii = random.randrange(2, (len(self.mapList[i]) - 2))
            if self.mapList[i][ii] == "F":
                self.mapList[i][ii] = iii
                iii += 1
        return self.mapList
