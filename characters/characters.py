import sys
from os.path import abspath, normpath, dirname, join

app_dir = abspath(join(dirname(__file__), ".."))
sys.path.insert(0, app_dir)

from kivy.graphics import Rectangle

from config import Config
from utils import Position, Size



class CharacterType:
    MAIN = 'main'
    ENEMY = 'enemy'


class Character():
    representation = None
    position = None
    size = None

    def __init__(self, x, y, width, height):
        self.position = Position(x, y)
        self.size = Size(width, height)

    def update_position(self, x, y):
        self.position.x = x
        self.position.y = y
        self.representation.pos = self.position.get_tuple()


class MainCharacter(Character):
    IMAGE_REPRESENTATION = 'ghost.jpeg'

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.representation = Rectangle(source=Config.MAIN_CHARACTER_IMAGE_REPRESENTATION,
                                        pos=self.position.get_tuple(),
                                        size=self.size.get_tuple())


class Enemy(Character):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.representation = Rectangle(pos=self.position.get_tuple(),
                                        size=self.size.get_tuple())
