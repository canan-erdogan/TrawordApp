from kivy.uix.button import Button
from kivy.lang import Builder
Builder.load_file("kv/history_button.kv")

class HistoryButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

