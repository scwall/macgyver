from structures.roadpictures import road_pictures


def test_roadpictures():
    assert road_pictures("pictures", "environment",
                         "test.png") == "/home/scwall/PycharmProjects/macgyver/test/pictures/environment/test.png"
