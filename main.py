from structure.loadMap import loadMap

# Help MacGyver to escape

mapgame = loadMap(1)
mapgame.readFolderMap()
mapgame.createMapList()

print(mapgame.getMap)
