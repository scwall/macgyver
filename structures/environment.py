from pygame import *
from structures.roadpictures import roadPictures


class Environment:
    def __init__(self, picture):
        self.image = image.load(roadPictures("pictures", "environment", picture)).convert()
        self.rect = self.image.get_rect()
