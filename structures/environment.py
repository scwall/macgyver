from pygame import *
from structures.roadospath import road_os_path


# Loading the surface of the image and loading the rectangular surface of the image
class Environment:
    def __init__(self, picture):
        self.image = image.load(road_os_path("pictures", "environment", picture)).convert()
        self.rect = self.image.get_rect()

    def set_environment_rect(self, x, y):
        self.rect.x = x
        self.rect.y = y
