from pygame import *
import pygame, os, sys, random
from structure.loadmap import LoadMap
from structure.variables import *
# Initialise Class for Windows main
class WindowsMain(LoadMap):

    def __init__(self, width=640, height=480):
        pygame.init()
        LoadMap.__init__(self)
        self.width = width
        self.height = height
        self.image = "pictures/background.png"
        self.background = pygame.image.load(self.image)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.display = pygame.display.set_caption(title_main)
        self.flip = pygame.display.flip()
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
                    self.screen.blit(self.background, ((i * 20),(ii * 20)))
                ii += 1
            ii = 0
            i += 1

    def mainloop(self):
        continuer = True

        # Boucle infinie
        while continuer:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = False
                if event.type == KEYDOWN and event.key == K_SPACE:
                    print("Espace")
                    # Constructor. Pass in the color of the block,

