import os
from os.path import abspath, normpath, dirname, join

base_path = normpath(join(abspath(dirname(__file__))))

class Config:

    LEVEL_MOVEMENT_RATE = 200
    LEVEL_UPDATE_TIME_INTERVAL = 0  # 0: Check on every frame, N: Chek every N seconds

    MAIN_CHARACTER_IMAGE_REPRESENTATION = join(base_path, 'assets/ghost.jpeg')
