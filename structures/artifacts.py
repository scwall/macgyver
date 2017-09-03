# Trouver image pour la seringle
from pygame import *
from structures.roadpictures import roadPictures
import os


class Artifacts:
    white = (255, 255, 255)

    def __init__(self):
        self.dic = {}
        self.dic_rect = {}
        i = 0
        for picture_tuple in os.listdir(os.path.join('pictures', 'artifacts')):
            self.image = image.load(roadPictures("pictures", "artifacts", picture_tuple)).convert()
            self.image.set_colorkey((255, 255, 255))
            self.rect = self.image.get_rect()
            self.dic[i] = self.image
            self.dic_rect[i] = self.rect
            i += 1
        self.scorestart = 0
        self.scoreend = len(self.dic.keys())
        self.display_artifact_font = font.SysFont("Arial", 15, bold=True, italic=False)
        self.display_artifact = self.display_artifact_font.render(
            'Numbers artifacts {0} / {1}'.format(self.scorestart, self.scoreend), True,
            self.white)

    def remove_objet(self, number):
        if number in self.dic.keys():
            del self.dic[number]
            del self.dic_rect[number]

    def score_objet(self):
        self.scorestart += 1
        self.display_artifact = self.display_artifact_font.render(
            'Numbers artifacts {0} / {1}'.format(self.scorestart, self.scoreend), True,
            self.white)

    def get_dic(self, values):
        return self.dic[values]

    def get_dic_rect(self, values):
        return self.dic_rect[values]

    def set_dic_rect(self, values, x, y):

        self.dic_rect[values].x = x
        self.dic_rect[values].y = y
