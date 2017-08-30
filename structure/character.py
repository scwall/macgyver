from os import path

import pygame
from pygame import *


class Character:
    def __init__(self, down, up, left, right,picturefolder):
        self.live = True
        self.picturefolder = picturefolder
        self.characterDown = pygame.image.load(self.roadPictures(str(down))).convert()
        self.characterDown.set_colorkey((255, 255, 255))

        self.characterUp = pygame.image.load(self.roadPictures(str(up))).convert()
        self.characterUp.set_colorkey((255, 255, 255))

        self.characterLeft = pygame.image.load(self.roadPictures(str(left))).convert()
        self.characterLeft.set_colorkey((255, 255, 255))

        self.characterRight = pygame.image.load(self.roadPictures(str(right))).convert()
        self.characterRight.set_colorkey((255, 255, 255))
        self.characterRect = self.characterRight.get_rect()

    def roadPictures(self, fichier):
        return path.join('pictures',self.picturefolder,fichier)

    def moveCharacter(self, directions, speed):
        if directions == "right":
            self.characterRect.x += int(speed)
        if directions == "left":
            self.characterRect.x -= int(speed)
        if directions == "up":
            self.characterRect.y -= int(speed)
        if directions == "down":
            self.characterRect.y += int(speed)
