import os

import pygame


class Environment():
    def __init__(self, picture):
        self.image = pygame.image.load(self.roadPictures(str(picture))).convert()
        self.rect = self.image.get_rect()

    def roadPictures(self, fichier):
        return os.path.join('pictures','environment', fichier)



