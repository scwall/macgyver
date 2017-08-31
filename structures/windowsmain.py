import os
from pygame import *
from structures.boss import Boss
from structures.environment import Environment
from structures.hero import Hero
from structures.loadmap import LoadMap
from structures.artifacts import Artifacts


# Initialise Class for Windows main
class WindowsMain:
    def __init__(self, width=680, height=822):
        init()
        self.width = width
        self.height = height
        self.win_or_lose = None
        self.SpriteCreate = False
        self.screen = display.set_mode((self.width, self.height))
        self.display = display.set_caption("Help MacGyver to escape")
        self.background = Environment("background.png")
        self.hero = Hero("down_hero.png", "up_hero.png", "left_hero.png", "right_hero.png")
        self.boss = Boss("down_boss.png", "up_boss.png", "left_boss.png", "right_boss.png")
        self.wall = Environment("wall.png")
        self.wall_list = list()
        self.floor = Environment("floor.png")
        self.artifacts = Artifacts()
        self.loadmap = LoadMap(level=1)
        self.loadmap.readFolderMap()
        self.loadmap.createMapList()
        self.screenSprite()
        display.flip()
        key.set_repeat(5, 50)

    def screenSprite(self):
        index_list_one = 0
        index_list_two = 0

        while index_list_one != len(self.loadmap.mapList):
            while index_list_two != len(self.loadmap.mapList[index_list_one]):
                x = index_list_two * 40
                y = index_list_one * 40 + 142
                self.floor = Environment("floor.png")
                self.floor.rect.x = x
                self.floor.rect.y = y
                self.screen.blit(self.floor.image, self.floor.rect)
                if self.loadmap.mapList[index_list_one][index_list_two] == "W":
                    self.wall = Environment("wall.png")
                    self.wall.rect.x = x
                    self.wall.rect.y = y
                    self.wall_list.append(self.wall.rect)
                    self.screen.blit(self.wall.image, self.wall.rect)
                if self.loadmap.mapList[index_list_one][index_list_two] == "B":
                    self.boss.characterRect.x = x
                    self.boss.characterRect.y = y
                    self.screen.blit(self.boss.characterUp, self.boss.characterRect)
                if self.loadmap.mapList[index_list_one][index_list_two] == "C" and self.SpriteCreate is False:
                    self.hero.characterRect.x = x
                    self.hero.characterRect.y = y
                    self.screen.blit(self.hero.characterDown, self.hero.characterRect)
                if self.loadmap.mapList[index_list_one][index_list_two] in self.artifacts.list.keys():
                    valuekeys = self.loadmap.mapList[index_list_one][index_list_two]
                    self.artifacts.list_rect[valuekeys].x = x
                    self.artifacts.list_rect[valuekeys].y = y
                    self.screen.blit(self.artifacts.list[valuekeys], self.artifacts.list_rect[valuekeys])

                index_list_two += 1
            index_list_two = 0
            index_list_one += 1
        self.SpriteCreate = True

    def detect_collision(self, types, direction=None):
        if types == "wall":
            if self.hero.characterRect.collidelist(self.wall_list) > 0:
                self.hero.moveCharacter(direction, -40)
        if types == "artefact":
            collide_test_dic = self.hero.characterRect.collidedict(self.artifacts.list_rect, 1)
            if collide_test_dic != None:
                if collide_test_dic[0] in self.artifacts.list.keys():
                    self.artifacts.removeObjet(collide_test_dic[0])
                    self.artifacts.scoreobjet()

        if types == "boss":
            if self.hero.characterRect.colliderect(self.boss.characterRect):
                if self.artifacts.scorestart == self.artifacts.scoreend:
                    self.win_or_lose = True
                else:
                    self.win_or_lose = False

    def mainloop(self):
        continues = True
        while continues:
            self.screen.blit(self.background.image, (0, 0))
            self.screen.blit(self.artifacts.display_artifact, (400, 10))
            for events in event.get():
                if events.type == QUIT:
                    continues = False

                if events.type == KEYDOWN and events.key == K_RIGHT and self.win_or_lose == None:
                    self.hero.moveCharacter("right", 40)
                    self.detect_collision("wall", "right")
                    self.detect_collision("artefact")
                    self.detect_collision("boss")
                    self.screenSprite()
                    self.screen.blit(self.hero.characterRight, self.hero.characterRect)

                if events.type == KEYDOWN and events.key == K_LEFT and self.win_or_lose == None:
                    self.hero.moveCharacter("left", 40)
                    self.detect_collision("wall", "left")
                    self.detect_collision("artefact")
                    self.detect_collision("boss")
                    self.screenSprite()
                    self.screen.blit(self.hero.characterLeft, self.hero.characterRect)

                if events.type == KEYDOWN and events.key == K_DOWN and self.win_or_lose == None:
                    self.hero.moveCharacter("down", 40)
                    self.detect_collision("wall", "down")
                    self.detect_collision("artefact")
                    self.detect_collision("boss")
                    self.screenSprite()
                    self.screen.blit(self.hero.characterDown, self.hero.characterRect)

                if events.type == KEYDOWN and events.key == K_UP and self.win_or_lose == None:
                    self.hero.moveCharacter("up", 40)
                    self.detect_collision("wall", "up")
                    self.detect_collision("artefact")
                    self.detect_collision("boss")
                    self.screenSprite()
                    self.screen.blit(self.hero.characterUp, self.hero.characterRect)
            if self.win_or_lose is True:
                print("win")
                continues = False
            if self.win_or_lose is False:
                print("lose")
                continues = False

            display.flip()
