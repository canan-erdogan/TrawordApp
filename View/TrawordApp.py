
from kivy import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

from View.traword_box import TrawordBox

Builder.load_file("kv/traword.kv")


class Traword(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(TrawordBox())


class TrawordApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Traword()


if __name__ == "__main__":
    TrawordApp().run()