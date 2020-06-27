from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

# Axis-Aligned Bounding Box
def collides(element_1, element_2):
    e1x = element_1[0][0]
    e1y = element_1[0][1]

    e2x = element_2[0][0]
    e2y = element_2[0][1]

    e1w = element_1[1][0]
    e1h = element_1[1][1]

    e2w = element_2[1][0]
    e2h = element_2[1][1]

    if (e1x < e2x + e2w and e1x + e1w > e2x and e1y < e2y + e2h and e1y + e1h > e2y):
        return True
    
    return False

class GameWidget(Widget):

    UP_KEY_CODE = 273
    DOWN_KEY_CODE = 274
    LEFT_KEY_CODE = 276
    RIGHT_KEY_CODE = 275
    SPACE_BAR_KEY_CODE = 32

    MOVEMENT_RATE = 200
    MOVEMENT_TIME_INTERVAL = 0  # 0: Check on every frame, 1: Chek every 1 second

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        with self.canvas:
            self.player = Rectangle(
                source="assets/ghost.jpeg", 
                pos=(0, 0), 
                size=(100, 100)
            )

            self.enemy = Rectangle(
                pos=(500, 0),
                size=(100,100)
            )

        self.keys_pressed = set()

        Clock.schedule_interval(self.move_step, 0)

        self.sound = SoundLoader.load('assets/sounds/background_main.wav')
        self.sound.play()

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, key_code, text, modifiers):
        code = int(key_code[0])
        self.keys_pressed.add(code)

        print("Key Code: {}, Key Text: {}".format(code, text))

    def _on_key_up(self, keyboard, key_code):
        code = key_code[0]
        if code in self.keys_pressed:
            self.keys_pressed.remove(code)

    def move_step(self, delta_time):
        current_x = self.player.pos[0]
        current_y = self.player.pos[1]

        step_size = self.MOVEMENT_RATE * delta_time

        if self.LEFT_KEY_CODE in self.keys_pressed:
            current_x = 0 if (current_x - step_size) < 0 else (current_x - step_size)

        if self.RIGHT_KEY_CODE in self.keys_pressed:
            current_x += step_size

        self.player.pos = (current_x, current_y)

        player = (self.player.pos, self.player.size)
        enemy = (self.enemy.pos, self.enemy.size)

        if collides(player, enemy):
            print('Collision detected!!')
        



class MyApp(App):
    def build(self):
        return GameWidget()


if __name__ == '__main__':
    app = MyApp()
    app.run()
