# Trouver image pour la seringle
from pygame import *
from structures.roadpictures import roadPictures
import os


class Artifacts:
    white = (255, 255, 255)

    def __init__(self):
        self.list = {}
        self.list_rect = {}
        i = 0
        for picture_tuple in os.listdir(os.path.join('pictures', 'artifacts')):
            self.image = image.load(roadPictures("pictures", "artifacts", picture_tuple)).convert()
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect()
            self.list[i] = self.image
            self.list_rect[i] = self.rect
            i += 1
        self.scorestart = 0
        self.scoreend = len(self.list.keys())
        self.display_artifact_font = font.SysFont("Arial", 15, bold=True, italic=False)
        self.display_artifact = self.display_artifact_font.render(
            'Numbers objects {0} / {1}'.format(self.scorestart, self.scoreend), True,
            self.white)

    def remove_objet(self, number):
        if number in self.list.keys():
            del self.list[number]
            del self.list_rect[number]

    def score_objet(self):
        self.scorestart += 1
        self.display_artifact = self.display_artifact_font.render(
            'Numbers objects {0} / {1}'.format(self.scorestart, self.scoreend), True,
            self.white)
