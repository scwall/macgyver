import random
import os
from structures.roadpictures import road_pictures


class LoadMap:
    # Create variables for instance
    def __init__(self, **level):
        self.map_list = []
        self.level = level["level"]
        self.map_read = str()

    # Read map in folder maps and choice of map
    def read_folder_map(self):
        level_map = road_pictures("maps", "level") + str(self.level)
        with open(level_map, "r") as map:
            self.map_read = map.read()

    # Create list on two level
    def create_map_list(self):
        list_build = []
        for level in self.map_read:
            if level is "\n":
                self.map_list.append(list(list_build))
                list_build = []
            else:
                list_build.append(level)
        self.random_objet()

    def random_objet(self):
        counter_object = 0
        while counter_object != len(os.listdir(os.path.join('pictures', 'artifacts'))):
            index_one = random.randrange(2, (len(self.map_list) - 2))
            index_two = random.randrange(2, (len(self.map_list[index_one]) - 2))
            if self.map_list[index_one][index_two] == "F":
                self.map_list[index_one][index_two] = counter_object
                counter_object += 1
        return self.map_list
