import pygame
from pygame import *
from structures.roadpictures import roadPictures


class Character:
    def __init__(self, down, up, left, right, picturefolder):
        self.live = True
        self.picturefolder = picturefolder
        self.characterDown = pygame.image.load(roadPictures("pictures", picturefolder, down)).convert()
        self.characterDown.set_colorkey((255, 255, 255))

        self.characterUp = pygame.image.load(roadPictures("pictures", picturefolder, up)).convert()
        self.characterUp.set_colorkey((255, 255, 255))

        self.characterLeft = pygame.image.load(roadPictures("pictures", picturefolder, left)).convert()
        self.characterLeft.set_colorkey((255, 255, 255))

        self.characterRight = pygame.image.load(roadPictures("pictures", picturefolder, right)).convert()
        self.characterRight.set_colorkey((255, 255, 255))
        self.characterRect = self.characterRight.get_rect()

    def move_character(self, directions, speed):
        if directions == "right":
            self.characterRect.x += int(speed)
        if directions == "left":
            self.characterRect.x -= int(speed)
        if directions == "up":
            self.characterRect.y -= int(speed)
        if directions == "down":
            self.characterRect.y += int(speed)
