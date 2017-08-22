from pygame import *
import pygame, os
from structure.loadmap import LoadMap
from structure.character import Character
# Initialise Class for Windows main
class WindowsMain(LoadMap,Character):

    def __init__(self, width=640,height=640):
        pygame.init()

        LoadMap.__init__(self)
        self.width = width
        self.height = height
        self.SpriteCreate = False
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.display = pygame.display.set_caption("Help MacGyver to escape")
        Character.__init__(self)
        self.boss = pygame.image.load(self.roadPictures('boss.png')).convert()
        self.boss.set_colorkey((255,255,255))
        self.bossRect = self.boss.get_rect()
        self.wall = pygame.image.load(self.roadPictures('wall.png')).convert()
        self.wallRect = self.wall.get_rect()
        self.floor = pygame.image.load(self.roadPictures('floor.png')).convert()
        self.floorRect = self.floor.get_rect()
        self.readFolderMap()
        self.createMapList()
        self.ScreenSprite()
        pygame.display.flip()
        pygame.key.set_repeat(5, 50)
    def roadPictures(self,fichier):
        return os.path.join('pictures',fichier)
    def ScreenSprite(self):
        i = 0
        ii = 0
        while i != len(self.mapList):
            while ii != len(self.mapList[i]):
                x = ii * 40
                y = i * 40

                if self.mapList[i][ii] == "W":
                    self.wallRect.x = x
                    self.wallRect.y = y
                    self.screen.blit(self.wall, self.wallRect)
                if self.mapList[i][ii] == "F" or self.mapList[i][ii] == "B" or self.mapList[i][ii] == "C":
                    self.floorRect.x = x
                    self.floorRect.y = y
                    self.screen.blit(self.floor,self.floorRect)
                if self.mapList[i][ii] == "B":
                    self.bossRect.x = x
                    self.bossRect.y = y
                    self.screen.blit(self.boss, self.bossRect)
                if self.mapList[i][ii] == "C" and self.SpriteCreate == False:
                    self.characterRect.x = x
                    self.characterRect.y = y
                    self.screen.blit(self.characterRight, self.characterRect)

                ii += 1
            ii = 0
            i += 1
        self.SpriteCreate = True

    def mainloop(self):
        continues = True

        while continues:
            for event in pygame.event.get():
                if event.type == QUIT:
                    continues = False
                if event.type == KEYDOWN and event.key == K_RIGHT:
                    self.moveCharacter("RIGHT")
                    self.ScreenSprite()
                    self.screen.blit(self.characterRight, self.characterRect)
                if event.type == KEYDOWN and event.key == K_LEFT:
                    self.moveCharacter("LEFT")
                    self.ScreenSprite()
                    self.screen.blit(self.characterLeft, self.characterRect)
                if event.type == KEYDOWN and event.key == K_DOWN:
                    self.moveCharacter("DOWN")
                    self.ScreenSprite()
                    self.screen.blit(self.characterDown, self.characterRect)
                if event.type == KEYDOWN and event.key == K_UP:
                    self.moveCharacter("UP")
                    self.ScreenSprite()
                    self.screen.blit(self.characterUp, self.characterRect)
            pygame.display.flip()
