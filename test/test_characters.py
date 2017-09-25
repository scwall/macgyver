from structures.character import Character
import pytest
from pygame import *

display.set_mode((100, 100))
display.set_caption("test_environment")

character = Character("test.png", "test.png", "test.png", "test.png", "character")
def test_character_rect():
    assert str(character.character_rect) == "<rect(0, 0, 40, 40)>"
def test_character_move():

    character.move_character("right", 10)
    assert str(character.character_rect) == "<rect(10, 0, 40, 40)>"
    character.move_character("left", 10)
    assert str(character.character_rect) == "<rect(0, 0, 40, 40)>"
    character.move_character("up", 10)
    assert str(character.character_rect) == "<rect(0, -10, 40, 40)>"
    character.move_character("down", 10)
    assert str(character.character_rect) == "<rect(0, 0, 40, 40)>"
def test_character_positioning():
    character.get_positioning("down")
    assert str(character.character_down) == "<Surface(40x40x32 SW)>"
    character.get_positioning("up")
    assert str(character.character_down) == "<Surface(40x40x32 SW)>"
    character.get_positioning("left")
    assert str(character.character_down) == "<Surface(40x40x32 SW)>"
    character.get_positioning("right")
    assert str(character.character_down) == "<Surface(40x40x32 SW)>"


