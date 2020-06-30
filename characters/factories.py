from abc import ABC, abstractmethod

from characters.characters import CharacterType, Character, MainCharacter, Enemy
from characters.records import CharacterRecord


# class CharacterFactory(ABC):
#     @abstractmethod
#     def create(self, character_record: CharacterRecord) -> Character:
#         pass


class CharacterFactory():
    @staticmethod
    def create(type: str, character_record: CharacterRecord) -> Character:

        if type == CharacterType.MAIN:
            return MainCharacter(x=character_record.x,
                                y=character_record.y,
                                width=character_record.width,
                                height=character_record.height)
        
        if type == CharacterType.ENEMY:
            return Enemy(x=character_record.x,
                                y=character_record.y,
                                width=character_record.width,
                                height=character_record.height)
        
        raise Exception('Invalid Character Type: {}'.format(type))

