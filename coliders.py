from abc import ABC, abstractmethod

from characters.characters import Character

class CollidDetector:
    @staticmethod
    def collides(character1: Character, character2: Character) -> bool: 
        if character1.position.x < (character2.position.x + character2.size.width) and \
           (character1.position.x + character1.size.width) > character2.position.x and \
           character1.position.y < (character2.position.y + character2.size.height) and \
           character1.position.y + character1.size.height > character2.position.y:
            return True

        return False
