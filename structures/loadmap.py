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
        counter_object = 0
        while counter_object != len(os.listdir(os.path.join('pictures', 'artifacts'))):
            index_one = random.randrange(2, (len(self.mapList) - 2))
            index_two = random.randrange(2, (len(self.mapList[index_one]) - 2))
            if self.mapList[index_one][index_two] == "F":
                self.mapList[index_one][index_two] = counter_object
                counter_object += 1
        return self.mapList
