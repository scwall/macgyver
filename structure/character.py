
from pygame import *
import os, pygame
class Character:
    def __init__(self):
        self.characterDown = pygame.image.load(self.roadPictures('down_character.png')).convert()
        self.characterDown.set_colorkey((255,255,255))
        self.characterRect = self.characterDown.get_rect()

        self.characterUp = pygame.image.load(self.roadPictures('up_character.png')).convert()
        self.characterUp.set_colorkey((255, 255, 255))
        #self.characterUpRect = self.characterUp.get_rect()

        self.characterLeft = pygame.image.load(self.roadPictures('left_character.png')).convert()
        self.characterLeft.set_colorkey((255, 255, 255))
        #self.characterLeftRect = self.characterLeft.get_rect()

        self.characterRight = pygame.image.load(self.roadPictures('right_character.png')).convert()
        self.characterRight.set_colorkey((255, 255, 255))
        #self.characterRightRect = self.characterRight.get_rect()

    def roadPictures(self,fichier):
        return os.path.join('pictures',fichier)

    def moveCharacter(self,directions):
        if directions == "RIGHT":
            self.characterRect.x += 3
        if directions == "LEFT":
            self.characterRect.x -= 3
        if directions == "UP":
            self.characterRect.y -= 3
        if directions == "DOWN":
            self.characterRect.y += 3
