from structures.environment import Environment
from structures.hero import Hero


class Test_environment(Environment):
    def __init__(self):
        super().__init__("testdrive.png")
