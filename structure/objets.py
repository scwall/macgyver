# Trouver image pour la seringle
import os
import random
import pygame
from structure.loadmap import LoadMap


class Objet():
    def __init__(self, *picture):
        self.list = {}
        self.list_rect = {}
        i = 0
        for picture_tuple in picture:
            self.image = pygame.image.load(self.roadPictures(str(picture_tuple))).convert()
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect()
            self.list[i] = self.image
            self.list_rect[i] = self.rect
            i += 1

    def roadPictures(self, fichier):
        return os.path.join('pictures', fichier)

    def randomObjet(self, map):
        maplist = list(map)
        iii = 0
        while iii != len(self.list):
            i = random.randrange(2, (len(maplist) - 2))
            ii = random.randrange(2, (len(maplist[i]) - 2))
            if maplist[i][ii] == "F":
                maplist[i][ii] = iii
                iii += 1
            print(maplist)
        return maplist

    def removeObjet(self, number):
        if number in self.list.keys():
            del self.list[number]
