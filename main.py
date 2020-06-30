from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

from config import Config
from coliders import CollidDetector
from characters.characters import CharacterType, MainCharacter, Enemy
from characters.factories import CharacterFactory
from characters.records import CharacterRecord

class GameWidget(Widget):

    UP_KEY_CODE = 273
    DOWN_KEY_CODE = 274
    LEFT_KEY_CODE = 276
    RIGHT_KEY_CODE = 275
    SPACE_BAR_KEY_CODE = 32

    # PLAYER_VELOCITY = 2
    # GRAVITY = -2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        player_record = CharacterRecord()
        player_record.x = 0
        player_record.y = 0
        player_record.width = 100
        player_record.height = 100

        self.player = CharacterFactory.create(CharacterType.MAIN, player_record)

        enemy_record = CharacterRecord()
        enemy_record.x = 500
        enemy_record.y = 0
        enemy_record.width = 100
        enemy_record.height = 100

        self.enemy = CharacterFactory.create(CharacterType.ENEMY, enemy_record)

        self.canvas.add(self.player.representation)
        self.canvas.add(self.enemy.representation)
        

        self.keys_pressed = set()

        Clock.schedule_interval(self.update, Config.LEVEL_UPDATE_TIME_INTERVAL)

        # self.sound = SoundLoader.load('assets/sounds/background_main.wav')
        # self.sound.play()

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, key_code, text, modifiers):
        code = int(key_code[0])
        self.keys_pressed.add(code)

    def _on_key_up(self, keyboard, key_code):
        code = key_code[0]
        if code in self.keys_pressed:
            self.keys_pressed.remove(code)

    def update(self, delta_time):
        current_x = self.player.position.x
        current_y = self.player.position.y

        step_size = Config.LEVEL_MOVEMENT_RATE * delta_time

        if self.LEFT_KEY_CODE in self.keys_pressed:
            current_x = 0 if (current_x - step_size) < 0 else (current_x - step_size)

        if self.RIGHT_KEY_CODE in self.keys_pressed:
            current_x += step_size

        if self.SPACE_BAR_KEY_CODE in self.keys_pressed: 
            # current_x = current_x + step_size
            current_y = current_y + (step_size * 10)

        self.player.update_position(current_x, current_y)

        if CollidDetector.collides(self.player, self.enemy):
            print('Collision detected!!')
        



class MyApp(App):
    def build(self):
        return GameWidget()


if __name__ == '__main__':
    app = MyApp()
    app.run()
