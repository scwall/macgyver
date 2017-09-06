import pygame
from pygame import *
from structures.roadpictures import road_pictures


# Loading the surface of the image and loading the rectangular surface of the image
class Character:
    def __init__(self, down, up, left, right, picturefolder):
        self.live = True
        self.picture_folder = picturefolder
        self.character_down = pygame.image.load(road_pictures("pictures", picturefolder, down)).convert()
        self.character_down.set_colorkey((255, 255, 255))

        self.character_up = pygame.image.load(road_pictures("pictures", picturefolder, up)).convert()
        self.character_up.set_colorkey((255, 255, 255))

        self.character_left = pygame.image.load(road_pictures("pictures", picturefolder, left)).convert()
        self.character_left.set_colorkey((255, 255, 255))

        self.character_right = pygame.image.load(road_pictures("pictures", picturefolder, right)).convert()
        self.character_right.set_colorkey((255, 255, 255))
        self.character_rect = self.character_right.get_rect()

    def move_character(self, directions, speed):
        """
        This method allows the character to move in one direction,
        as well as the speed of movement per square (pixel size of the image)
        :param directions:
        Direction up, down, left, right
        :param speed:
        Movement speed
        """
        if directions == "right":
            self.character_rect.x += int(speed)
        if directions == "left":
            self.character_rect.x -= int(speed)
        if directions == "up":
            self.character_rect.y -= int(speed)
        if directions == "down":
            self.character_rect.y += int(speed)

    def set_character_rect(self, x, y):
        self.character_rect.x = x
        self.character_rect.y = y

    @property
    def get_character_rect(self):
        return self.character_rect

    def get_positioning(self, positioning):
        if positioning is "down":
            return self.character_down
        if positioning is "up":
            return self.character_up
        if positioning is "left":
            return self.character_left
        if positioning is "right":
            return self.character_right
