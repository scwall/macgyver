from pygame import *
from structures.roadpictures import roadPictures

#Loading the surface of the image and loading the rectangular surface of the image
class Environment:
    def __init__(self, picture):
        print(roadPictures("pictures", "environment", picture))
        self.image = image.load(roadPictures("pictures", "environment", picture)).convert()
        self.rect = self.image.get_rect()

    def set_environment_rect(self, x, y):
        self.rect.x = x
        self.rect.y = y
