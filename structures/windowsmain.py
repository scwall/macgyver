from pygame import *
from structures.artifacts import Artifacts
from structures.boss import Boss
from structures.environment import Environment
from structures.hero import Hero
from structures.loadmap import LoadMap


# Initialise Class for Windows main
class WindowsMain:
    def __init__(self, width=680, height=822):
        init()
        self.width = width
        self.height = height
        self.SpriteCreate = False
        self.screen = display.set_mode((self.width, self.height))
        self.display = display.set_caption("Help MacGyver to escape")
        self.background = Environment("background.png")
        self.win_or_lose = None
        self.wall_list = list()
        self.win = Environment("win.png")
        self.win.image.set_colorkey((255, 255, 255))
        self.lose = Environment("lose.png")
        self.lose.image.set_colorkey((255, 255, 255))
        self.hero = Hero("down_hero.png", "up_hero.png", "left_hero.png", "right_hero.png")
        self.boss = Boss("down_boss.png", "up_boss.png", "left_boss.png", "right_boss.png")
        self.wall = Environment("wall.png")
        self.floor = Environment("floor.png")
        self.artifacts = Artifacts()
        self.loadmap = LoadMap(level=1)
        self.loadmap.readFolderMap()
        self.loadmap.createMapList()
        self.screensprite()
        display.flip()
        key.set_repeat(5, 50)

    def screensprite(self):
        """
        This method calculates the index of each list and looks at the letter of the map,
        it then creates the sprites of the environment and the appliques to the rectangle drawn by
        contribution to the size of the sprite. True or False is added to the hero
        so that it is not drawn every time the map is redrawn
        """
        index_list_one = 0
        index_list_two = 0

        while index_list_one != len(self.loadmap.mapList):
            while index_list_two != len(self.loadmap.mapList[index_list_one]):
                x = index_list_two * 40
                y = index_list_one * 40 + 142
                self.floor = Environment("floor.png")
                self.floor.set_environment_rect(x, y)
                self.screen.blit(self.floor.image, self.floor.rect)
                if self.loadmap.mapList[index_list_one][index_list_two] == "W":
                    self.wall = Environment("wall.png")
                    self.wall.set_environment_rect(x, y)
                    self.wall_list.append(self.wall.rect)
                    self.screen.blit(self.wall.image, self.wall.rect)
                if self.loadmap.mapList[index_list_one][index_list_two] == "B":
                    self.boss.set_character_rect(x, y)
                    self.screen.blit(self.boss.get_positioning("up"), self.boss.get_character_rect)
                if self.loadmap.mapList[index_list_one][index_list_two] == "C" and self.SpriteCreate is False:
                    self.hero.set_character_rect(x, y)
                    self.screen.blit(self.hero.get_positioning("down"), self.hero.get_character_rect)
                if self.loadmap.mapList[index_list_one][index_list_two] in self.artifacts.dic.keys():
                    valuekeys = self.loadmap.mapList[index_list_one][index_list_two]
                    self.artifacts.set_dic_rect(valuekeys, x, y)
                    self.screen.blit(self.artifacts.get_dic(valuekeys), self.artifacts.get_dic_rect(valuekeys))

                index_list_two += 1
            index_list_two = 0
            index_list_one += 1
        self.SpriteCreate = True

    def detect_collision(self, types, direction=None):
        """
        This method allows the detection of collision between object:
        :param types:
        Defined the type of the object, as for example if there is collision with the boss,
        it will look if all objects have been collected
        :param direction:
        Defined the direction of the character to prevent it from entering an object
        """
        if types == "wall":
            if self.hero.character_rect.collidelist(self.wall_list) > 0:
                self.hero.move_character(direction, -40)
        if types == "artefact":
            collide_test_dic = self.hero.character_rect.collidedict(self.artifacts.dic_rect, 1)
            if collide_test_dic is not None:
                if collide_test_dic[0] in self.artifacts.dic.keys():
                    self.artifacts.remove_objet(collide_test_dic[0])
                    self.artifacts.score_objet()
        if types == "boss":
            if self.hero.character_rect.colliderect(self.boss.character_rect):
                if self.artifacts.scorestart == self.artifacts.scoreend:
                    self.win_or_lose = True
                else:
                    self.win_or_lose = False

    def mainloop(self):
        """
       Main loop of the game, here we analyze the keys pressed,
       the closing of the window, the collisions between object and if the hero has lost or win
        """
        continues = True
        while continues:
            self.screen.blit(self.background.image, (0, 0))
            self.screen.blit(self.artifacts.display_artifact, (475, 80))

            for events in event.get():
                if events.type == QUIT:
                    continues = False

                if events.type == KEYDOWN and events.key == K_RIGHT:
                    if self.win_or_lose is None:
                        self.hero.move_character("right", 40)
                        self.detect_collision("wall", "right")
                        self.detect_collision("artefact")
                        self.detect_collision("boss")
                        self.screensprite()
                        self.screen.blit(self.hero.get_positioning("right"), self.hero.get_character_rect)
                if events.type == KEYDOWN and events.key == K_LEFT:
                    if self.win_or_lose is None:
                        self.hero.move_character("left", 40)
                        self.detect_collision("wall", "left")
                        self.detect_collision("artefact")
                        self.detect_collision("boss")
                        self.screensprite()
                        self.screen.blit(self.hero.get_positioning("left"), self.hero.get_character_rect)
                if events.type == KEYDOWN and events.key == K_DOWN:
                    if self.win_or_lose is None:
                        self.hero.move_character("down", 40)
                        self.detect_collision("wall", "down")
                        self.detect_collision("artefact")
                        self.detect_collision("boss")
                        self.screensprite()
                        self.screen.blit(self.hero.get_positioning("down"), self.hero.get_character_rect)
                if events.type == KEYDOWN and events.key == K_UP:
                    if self.win_or_lose is None:
                        self.hero.move_character("up", 40)
                        self.detect_collision("wall", "up")
                        self.detect_collision("artefact")
                        self.detect_collision("boss")
                        self.screensprite()
                        self.screen.blit(self.hero.get_positioning("up"), self.hero.get_character_rect)
            if self.win_or_lose is True:
                self.screen.blit(self.win.image, (100, 300))

            if self.win_or_lose is False:
                self.screen.blit(self.lose.image, (10, 300))

            display.flip()
