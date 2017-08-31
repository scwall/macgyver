import os
import pygame
from structures.roadpictures import roadPictures

class Environment():
    def __init__(self, picture):
        self.image = pygame.image.load(roadPictures("pictures","environment",picture)).convert()
        self.rect = self.image.get_rect()



