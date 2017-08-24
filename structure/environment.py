import os

import pygame


class Environment(pygame.sprite.Sprite):
    def __init__(self, picture):
        super().__init__()
        self.image = pygame.image.load(self.roadPictures(str(picture))).convert()
        self.rect = self.image.get_rect()

    def roadPictures(self, fichier):
        return os.path.join('pictures', fichier)
