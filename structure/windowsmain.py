import pygame
from pygame import *
from structure.boss import Boss
from structure.environment import Environment
from structure.hero import Hero
from structure.loadmap import LoadMap
from structure.objets import Objet


# Initialise Class for Windows main
class WindowsMain():
    def __init__(self, width=640, height=640):
        pygame.init()

        self.width = width
        self.height = height
        self.SpriteCreate = False
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.display = pygame.display.set_caption("Help MacGyver to escape")
        self.hero = Hero("down_hero.png", "up_hero.png", "left_hero.png", "right_hero.png")
        self.boss = Boss("down_boss.png", "up_boss.png", "left_boss.png", "right_boss.png")
        self.wall = Environment("wall.png")
        self.wall_list = list()
        self.floor = Environment("floor.png")
        self.objet = Objet("fishing_rod.png", "pestle.png")
        self.objet_list = dict()
        self.loadmap = LoadMap(level=1)
        self.loadmap.readFolderMap()
        self.loadmap.createMapList()
        self.loadmap.mapList = self.objet.randomObjet(self.loadmap.mapList)
        self.ScreenSprite()
        pygame.display.flip()
        pygame.key.set_repeat(5, 50)

    def roadPictures(self, fichier):

        return os.path.join('pictures', fichier)

    def ScreenSprite(self):
        i = 0
        ii = 0
        iii = 0
        while i != len(self.loadmap.mapList):
            while ii != len(self.loadmap.mapList[i]):
                x = ii * 40
                y = i * 40
                self.floor = Environment("floor.png")
                self.floor.rect.x = x
                self.floor.rect.y = y
                self.screen.blit(self.floor.image, self.floor.rect)
                if self.loadmap.mapList[i][ii] == "W":
                    self.wall = Environment("wall.png")
                    self.wall.rect.x = x
                    self.wall.rect.y = y
                    self.wall_list.append(self.wall.rect)
                    self.screen.blit(self.wall.image, self.wall.rect)

                if self.loadmap.mapList[i][ii] == "B":
                    self.boss.characterRect.x = x
                    self.boss.characterRect.y = y
                    self.screen.blit(self.boss.characterUp, self.boss.characterRect)
                if self.loadmap.mapList[i][ii] == "C" and self.SpriteCreate == False:
                    self.hero.characterRect.x = x
                    self.hero.characterRect.y = y
                    self.screen.blit(self.hero.characterDown, self.hero.characterRect)
                if self.loadmap.mapList[i][ii] in self.objet.list.keys():
                    valuekeys = self.loadmap.mapList[i][ii]
                    self.objet.list_rect[valuekeys].x = x
                    self.objet.list_rect[valuekeys].y = y
                    # self.objet_list.append(self.objet.list_rect[valuekeys])
                    self.objet_list[valuekeys] = self.objet.list_rect[valuekeys]
                    self.screen.blit(self.objet.list[valuekeys], self.objet.list_rect[valuekeys])
                iii += 1
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
                    self.hero.moveCharacter("RIGHT", 40)
                    if self.hero.characterRect.collidelist(self.wall_list) > 0:
                        self.hero.moveCharacter("RIGHT", -40)
                    collide_test_dic = self.hero.characterRect.collidedict(self.objet_list, 1)
                    if collide_test_dic != None:
                        if collide_test_dic[0] in self.objet_list.keys():
                            self.objet.removeObjet(collide_test_dic[0])
                    self.ScreenSprite()
                    self.screen.blit(self.hero.characterRight, self.hero.characterRect)

                if event.type == KEYDOWN and event.key == K_LEFT:
                    self.hero.moveCharacter("LEFT", 40)
                    if self.hero.characterRect.collidelist(self.wall_list) > 0:
                        self.hero.moveCharacter("LEFT", -40)
                    collide_test_dic = self.hero.characterRect.collidedict(self.objet_list, 1)
                    if collide_test_dic != None:
                        if collide_test_dic[0] in self.objet_list.keys():
                            self.objet.removeObjet(collide_test_dic[0])
                    self.ScreenSprite()
                    self.screen.blit(self.hero.characterLeft, self.hero.characterRect)

                if event.type == KEYDOWN and event.key == K_DOWN:
                    self.hero.moveCharacter("DOWN", 40)
                    if self.hero.characterRect.collidelist(self.wall_list) > 0:
                        self.hero.moveCharacter("DOWN", -40)
                    collide_test_dic = self.hero.characterRect.collidedict(self.objet_list, 1)
                    if collide_test_dic != None:
                        if collide_test_dic[0] in self.objet_list.keys():
                            self.objet.removeObjet(collide_test_dic[0])
                    self.ScreenSprite()
                    self.screen.blit(self.hero.characterDown, self.hero.characterRect)

                if event.type == KEYDOWN and event.key == K_UP:
                    self.hero.moveCharacter("UP", 40)
                    if self.hero.characterRect.collidelist(self.wall_list) > 0:
                        self.hero.moveCharacter("UP", -40)
                    collide_test_dic = self.hero.characterRect.collidedict(self.objet_list, 1)
                    if collide_test_dic != None:
                        if collide_test_dic[0] in self.objet_list.keys():
                            self.objet.removeObjet(collide_test_dic[0])
                    self.ScreenSprite()
                    self.screen.blit(self.hero.characterUp, self.hero.characterRect)

            pygame.display.flip()
