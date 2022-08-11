from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from View.traword_box_content import TrawordBoxContent
from View.traword_box_title import TrawordBoxTitle

Builder.load_file("kv/traword_box.kv")


class TrawordBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(TrawordBoxTitle())
        self.add_widget(TrawordBoxContent())
