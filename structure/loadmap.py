class LoadMap:
    # Create variables for instance
    def __init__(self, **level):
        self.mapList = []
        self.level = level["level"]
        self.mapRead = str()

    # Read map in folder maps and choice of map
    def readFolderMap(self):
        levelMap = "maps/level" + str(self.level)
        with open(levelMap, "r") as map:
            self.mapRead = map.read()

    # Create list on two level
    def createMapList(self):
        listBuild = []
        for level in self.mapRead:
            if level is "\n":
                self.mapList.append(listBuild[:])
                listBuild = []
            else:
                listBuild.append(level)
