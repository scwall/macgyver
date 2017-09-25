from structures.roadospath import road_os_path


def test_roadpictures():
    assert road_os_path("pictures", "environment",
                         "test.png") == "/home/scwall/PycharmProjects/macgyver/test/pictures/environment/test.png"
