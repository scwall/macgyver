from pygame import *
import pygame, os, sys, random
from structure.loadmap import LoadMap
# Initialise Class for Windows main
class WindowsMain(LoadMap,pygame.sprite.Sprite):

    def __init__(self, width=640, height=640):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        LoadMap.__init__(self)
        self.width = width
        self.height = height
        self.wallpicture = "pictures/wall.png"
        self.floorpicture = "pictures/floor.png"
        self.bosspicture = "pictures/boss.png"
        self.boss = pygame.image.load(self.bosspicture)
        self.wall = pygame.image.load(self.wallpicture)
        self.floor = pygame.image.load(self.floorpicture)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.display = pygame.display.set_caption("Help MacGyver to escape")
        self.readFolderMap()
        self.createMapList()
        self.ScreenSprite()
        pygame.display.flip()

    def ScreenSprite(self):
        i = 0
        ii = 0
        while i != len(self.mapList):
            print(len(self.mapList))
            while ii != len(self.mapList[i]):
                if self.mapList[i][ii] == "W":
                    self.screen.blit(self.wall, ((i * 40),(ii * 40)))
                if self.mapList[i][ii] == "F":
                    self.screen.blit(self.floor, ((i * 40),(ii * 40)))
                if self.mapList[i][ii] == "B":
                    self.screen.blit(self.boss, ((i * 40), (ii * 40)))
                ii += 1
            ii = 0
            i += 1

    def mainloop(self):
        continues = True

        while continues:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continues = False
                if event.type == KEYDOWN and event.key == K_DOWN:
                    pass


