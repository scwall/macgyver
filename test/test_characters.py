from structures.character import Character
import pytest
from pygame import *

display.set_mode((100, 100))
display.set_caption("test_environment")


def test_character():
    character = Character("test.png", "test.png", "test.png", "test.png", "character")
    character.move_character("right", 10)
    assert str(character.character_rect) == "<rect(10, 0, 40, 40)>"
    character.move_character("left", 10)
    assert str(character.character_rect) == "<rect(0, 0, 40, 40)>"
    character.move_character("up", 10)
    assert str(character.character_rect) == "<rect(0, -10, 40, 40)>"
    character.move_character("down", 10)
    assert str(character.character_rect) == "<rect(0, 0, 40, 40)>"
