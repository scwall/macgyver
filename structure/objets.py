# Trouver image pour la seringle
import os
# import random
from pygame import *


class Objet():
    white = (255, 255, 255)

    def __init__(self):
        self.list = {}
        self.list_rect = {}
        i = 0
        for picture_tuple in os.listdir(os.path.join('pictures', 'artefacts')):
            self.image = image.load(self.roadPictures(str(picture_tuple))).convert()
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect()
            self.list[i] = self.image
            self.list_rect[i] = self.rect
            i += 1
        self.scorestart = 0
        self.scoreend = len(self.list.keys())
        self.display_artefact_font = font.SysFont("Arial", 15)
        self.display_artefact = self.display_artefact_font.render(
            'Number object {0} / {1}'.format(self.scorestart, self.scoreend), True,
            self.white)

    def roadPictures(self, fichier):
        return os.path.join('pictures', 'artefacts', fichier)

    def removeObjet(self, number):
        if number in self.list.keys():
            del self.list[number]
            del self.list_rect[number]

    def scoreobjet(self):
        self.scorestart += 1
        self.display_artefact = self.display_artefact_font.render(
            'Number object {0} / {1}'.format(self.scorestart, self.scoreend), True,
            self.white)

