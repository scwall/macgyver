import os


def road_pictures(*roadfile):
    return os.path.join(os.getcwd(), *roadfile)
