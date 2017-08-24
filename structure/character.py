
from pygame import *
import os, pygame
class Character:
    def __init__(self,down,up,left,right):
        self.live = True

        self.characterDown = pygame.image.load(self.roadPictures(str(down))).convert()
        self.characterDown.set_colorkey((255,255,255))


        self.characterUp = pygame.image.load(self.roadPictures(str(up))).convert()
        self.characterUp.set_colorkey((255, 255, 255))


        self.characterLeft = pygame.image.load(self.roadPictures(str(left))).convert()
        self.characterLeft.set_colorkey((255, 255, 255))


        self.characterRight = pygame.image.load(self.roadPictures(str(right))).convert()
        self.characterRight.set_colorkey((255, 255, 255))
        self.characterRect = self.characterRight.get_rect()

    def roadPictures(self,fichier):
        return os.path.join('pictures',fichier)

    def moveCharacter(self,directions,speed):
        if directions == "RIGHT":
            self.characterRect.x += int(speed)
        if directions == "LEFT":
            self.characterRect.x -= int(speed)
        if directions == "UP":
            self.characterRect.y -= int(speed)
        if directions == "DOWN":
            self.characterRect.y += int(speed)
