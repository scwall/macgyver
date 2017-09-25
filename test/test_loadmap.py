import pytest
from structures.roadospath import road_os_path
from structures.loadmap import LoadMap


def test_loadmap():
    test = LoadMap(level=1)
    test_level_map = road_os_path("maps", "level1")
    with open(test_level_map) as test_map:
        level1 = test_map.read()
    assert test.map_list[0][0] == level1[0]
