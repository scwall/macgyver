import random
import os
from structures.roadpictures import road_pictures


class LoadMap:
    # Create variables for instance
    def __init__(self, **level):
        self.mapList = []
        self.level = level["level"]
        self.mapRead = str()

    # Read map in folder maps and choice of map
    def read_folder_map(self):
        level_map = road_pictures("maps", "level") + str(self.level)
        with open(level_map, "r") as map:
            self.mapRead = map.read()

    # Create list on two level
    def create_map_list(self):
        list_build = []
        for level in self.mapRead:
            if level is "\n":
                self.mapList.append(list(list_build))
                list_build = []
            else:
                list_build.append(level)
        self.random_objet()

    def random_objet(self):
        counter_object = 0
        while counter_object != len(os.listdir(os.path.join('pictures', 'artifacts'))):
            index_one = random.randrange(2, (len(self.mapList) - 2))
            index_two = random.randrange(2, (len(self.mapList[index_one]) - 2))
            if self.mapList[index_one][index_two] == "F":
                self.mapList[index_one][index_two] = counter_object
                counter_object += 1
        return self.mapList
