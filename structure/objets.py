#Trouver image pour la seringle
import os

import pygame


class Objet():
    def __init__(self, *picture):
        self.list = []
        for picture_tuple in picture:
            self.image = pygame.image.load(self.roadPictures(str(picture_tuple))).convert()
            self.rect = self.image.get_rect()
            self.list.append(self.rect)
        print(self.list)
        print(self.image)

    def roadPictures(self, fichier):
        return os.path.join('pictures', fichier)


