from pygame import *
import pytest
from structures.environment import Environment

display.set_mode((100, 100))
display.set_caption("test_environment")


def test_environment():
    environment = Environment("test.png")

    environment.set_environment_rect(1, 2)

    assert str(environment.rect) == "<rect(1, 2, 40, 40)>"
